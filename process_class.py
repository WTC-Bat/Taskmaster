import os
import time
import threading
import subprocess
import tmfuncs
from tmlog import log

class Process(threading.Thread):
	""""""
	def __init__(self, progdict):
		threading.Thread.__init__(self)
		self.pop = None
		self.progd = progdict
		self.stdout = None
		self.stderr = None
		self.stop = False
		self.name = self.threadName()
		self.active = False
		self.retries = 0

	def run(self):
		"""
		threading.Thread.run() override. Invoked via threading.Thread.Start()
		"""
		args = self.progd["command"].split()	# or shlex.split()
		wkdir = None
		envs = None

		log("Starting process '" + self.name + "'", "./tmlog.txt", False)
		if (self.progd["workingdir"]):
			wkdir = self.progd["workingdir"]
		if (len(self.progd["envvars"]) > 0):
			envs = self.progd["envvars"]
		try:
			# self.pop = subprocess.Popen(args, stderr=subprocess.PIPE,
			# 							stdout=subprocess.PIPE)
			# self.pop = subprocess.Popen(args, cwd=wkdir, stderr=subprocess.PIPE,
			# 							stdout=subprocess.PIPE, env=envs)
			self.pop = subprocess.Popen(args, cwd=wkdir, stderr=subprocess.PIPE,
										stdout=subprocess.PIPE, env=envs,
										preexec_fn=self.initializeProcess)
		except (ValueError, OSError) as e:
			# print("Invalid arguments given to 'subprocess.Popen'")
			# print("Program Name: " + self.progd["progname"])
			log("Caught exception '" + str(e) + "'", "./tmlog.txt", False)
			return

		self.stop = False
		self.active = True
		self.monitor_timer()

	def monitor_timer(self):
		"""Monitor the state of this process every second"""
		tim = threading.Timer(1.0, self.monitor_timer)
		# tim = threading.Timer(0.1, self.monitor_timer)
		tim.start()
		self.pop.poll()
		if (self.stop == True):
			# signum = tmfuncs.getSignalValue(self.progd["stopsig"])
			tim.cancel()
			log("Stopping process '" + self.name + "'", "./tmlog.txt", False)
			# self.pop.send_signal(signum)
			self.active = False
			return
		if (self.pop.returncode != None):
			self.stop = True
			if (self.progd["restart"] == "always"):
				self.run()
				log("Restarting '" + self.name + "'", "./tmlog.txt", False)
			elif (self.progd["restart"] == "unexpected"):
				if (self.expectedReturnCode() == False
						and self.retries != int(self.progd["retries"])):
					self.retries += 1
					log("'" + self.name + "' terminated unexpectedly",
						"./tmlog.txt", False)
					self.run()
					log("Attempting to relaunch '" + self.name + "'",
						"./tmlog.txt", False)
					log("Retries: " + str(self.retries))
				else:
					self.stop = True
			else:
				self.stop = True

	def expectedReturnCode(self):
		"""
		Returns true if the return code from popen.poll() is an expected value
		"""
		for rcode in self.progd["exitcodes"]:
			if (rcode == self.pop.returncode):
				return (True)
		return (False)

	def initializeProcess(self):
		""""""
		os.setpgrp()
		# os.umask(format(self.progd["umask"], "03o"))
		# os.umask(077)
		os.umask(int(self.progd["umask"]))

	def threadName(self):
		"""Return a number for multiple processes of the same program"""
		idx = len(self.progd["processes"]) + 1
		tname = "Thread-" + self.progd["progname"] + "-" + str(idx)

		return (tname)


	def writeStdErr(self):
		"""
		Writes the processes standard error to the file specified in the
		program's 'stderr' element in the config file
		"""
		splt = ""
		outpath = ""

		if not (self.progd["stderr"]):
			outpath = "./" + self.progd["progname"] + ".stderr"
		splt = self.progd["stderr"].split(os.path.sep)
		if (len(splt) == 1):
			outpath = "./" + self.progd["stderr"]
		else:
			outpath = self.progd["stderr"]
		with open(outpath, "w") as out:	#with open(outpath, "a") as out:
			out.write(self.stderr)

	def writeStdOut(self):
		"""
		Writes the processes standard output to the file specified in the
		program's 'stdout' element in the config file
		"""
		splt = ""
		outpath = ""

		print("Write: " + self.name) #
		if not (self.progd["stdout"]):
			outpath = "./" + self.progd["progname"] + ".stdout"
		splt = self.progd["stdout"].split(os.path.sep)
		if (len(splt) == 1):
			outpath = "./" + self.progd["stdout"]
		else:
			outpath = self.progd["stdout"]
		with open(outpath, "w") as out:	#with open(outpath, "a") as out:
			# out.write(self.stdout)
			# out.write(self.pop.stdout.readline())
			out.write(self.pop.stdout.read())
