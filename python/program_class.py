# import array
import subprocess
import shlex
import os
import sched
import time
import threading
import process_class as procc
from tmlog import log

class Program():
	""""""
	def __init__(self, args=None):
		""""""
		self.progname = "TMProg"
		self.command = ""
		self.procnum = 1
		self.autolaunch = False
		self.starttime = 5
		self.restart = "never"
		self.retries = 3
		self.stopsig = "SIG"
		self.stoptime = 10
		self.exitcode = [0]
		self.envvars = dict
		self.workingdir = "./"
		self.umask = 022
		self.stdout = self.workingdir + self.progname + ".tm.stdout"
		self.stderr = self.workingdir + self.progname + ".tm.stderr"
		self.redout = False
		self.rederr = False
		self.processes = list()

		# print("UMASK: " + format(self.umask, "03o"))

		if type(args) is dict:
			for key, val in args.iteritems():
				if key == "progname":
					self.progname = val
				elif key == "command":
					self.command = val
				elif key == "procnum":
					self.procnum = val
				elif key == "autolaunch":
					self.autolaunch = val
				elif key == "starttime":
					self.starttime = val
				elif key == "restart":
					self.restart = val
				elif key == "retries":
					self.retries = val
				elif key == "stopsig":
					self.stopsig = val
				elif key == "stoptime":
					self.stoptime = val
				elif type(val) is list and key == "exitcodes":
					self.exitcodes = list()
					for i in val:
						self.exitcodes.append(i);
				elif key == "stdout":
					self.stdout = val
				elif key == "stderr":
					self.stderr = val
				elif key == "redout":
					self.redout = val
				elif key == "rederr":
					self.rederr = val
				elif type(val) is dict and key == "envvars":
					self.envvars = dict();
					for k, v in val.iteritems():
						self.envvars[k] = v
				elif key == "workingdir":
					self.workingdir = val
				elif key == "umask":
					self.umask = val
			log("Program '" + self.progname + "' initialized", "./tmlog.txt", False)

	def __str__(self):
		""""""
		return (("progname: {}\ncommand: {}\nprocnum: {}\nautolaunch: {}\n"
				"starttime: {}\nrestart: {}\nretries: {}\nstopsig: {}\n"
				"stoptime: {}\nexitcodes: {}\nstdout: {}\nstderr: {}\n"
				"redout: {}\nrederr: {}\nenvvars: {}\nworkingdir: {}\n"
				"umask: {}\n"))\
				.format(self.progname, self.command, self.procnum,
						self.autolaunch, self.starttime, self.restart,
						self.retries, self.stopsig, self.stoptime,
						self.exitcodes, self.stdout, self.stderr, self.redout,
						self.rederr, self.envvars, self.workingdir, self.umask)

	def __eq__(self, obj):
		""""""
		return (str(self) == str(obj))

	# def handleSignal(self, signum, frame):
	# 	""""""
	#
	# def registerSignal(self.stopsig):
	# 	""""""

	def runAndMonitor(self):
		""""""
		proc = procc.Process(self.__dict__)
		self.processes.append(proc)
		proc.start()
		log("Program '" + self.progname + "' process starting", "./tmlog.txt",
			False)
		time.sleep(0.3)	#!


		# self.process = procc.Process(self.__dict__)
		# self.process.start()
		# log("Program '" + self.progname + "' process starting", "./tmlog.txt",
		# 	False)
		# time.sleep(0.3)
