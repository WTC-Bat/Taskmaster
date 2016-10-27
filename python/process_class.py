import time
import threading
import subprocess
# import exceptions as exc
from tmlog import log

class Process(threading.Thread):
	""""""
	def __init__(self, progdict):
		threading.Thread.__init__(self)
		self.stdout = None
		self.stderr = None
		self.pop = None
		self.progd = progdict
		self.killprocess = False
		self.name = "Thread-" + self.progd["progname"]
		self.active = False
		self.retries = 0
		# self.tim = None
		log("Process '" + self.name + "' initialized", "./tmlog.txt", False)

	def run(self):
		""""""
		args = self.progd["command"].split()	# or shlex.split()
		try:
			self.pop = subprocess.Popen(args, stderr=subprocess.PIPE,
										stdout=subprocess.PIPE)
		except (ValueError, OSError) as e:
			print("Invalid arguments given to 'subprocess.Popen'")
			print("Program Name: " + self.progd["progname"])
			log("Caught exception '" + str(e) + "'", "./tmlog.txt", False)
			# self.retries += 1		?
			# self.run()			?
			# exit(1) to stop taskmaster entirely
			# - OR -
			return

		self.active = True
		self.monitor_timer()

	def monitor_timer(self):
		# self.active = True
		tim = threading.Timer(1.0, self.monitor_timer)
		tim.start()
		self.pop.poll()
		if (self.killprocess == True):
			tim.cancel()
			self.pop.terminate()
			log("Terminating '" + self.name + "'", "./tmlog.txt", False)
			return
		if (self.pop.returncode != None):
			self.active = False	#Here okay? Is it inactive at this point
			if (self.progd["restart"] == "always"):
				tim.cancel()
				log("'" + self.name + "' returned valid code", "./tmlog.txt",
					False)
				self.run()		#restart? will it work?
				log("Restarting '" + self.name + "'", "./tmlog.txt", False)
			elif (self.progd["restart"] == "unexpected"):
				if (self.expectedReturnCode() == False
						and self.retries != self.progd["retries"]):
					tim.cancel()
					self.retries += 1
					log("'" + self.name + "' terminated unexpectedly",
						"./tmlog.txt", False)
					self.run()	#restart? will it work?
					log("Attempting to relaunch '" + self.name + "'",
						"./tmlog.txt", False)
					log("Retries: " + str(self.retries))
			#terminate?

	def expectedReturnCode(self):
		"""Returns true if the return code from popen.poll() is """
		for rcode in self.progd["exitcodes"]:
			if (rcode == self.pop.returncode):
				return (True)
		return (False)

	# def handleSignal(self, signum, frame):
	# 	""""""
	# 	print("PROCESS CAUGHT SIGNAL")
	# 	self.pop.send_signal(signum)
	# 	self.killprocess = True
	#
	# def registerSignal(self):
	# 	""""""
	# 	signum = tmfuncs.getSignalValue(self.progd["stopsig"])
	# 	if (signum != -42):
	# 		signal.signal(signum, self.handleSignal)
