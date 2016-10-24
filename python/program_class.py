# import array
import subprocess
import shlex
import os
import sched
import time
import threading
import process_class as procc

class Program():
	""""""
	def __init__(self, args=None):
		""""""
		# self.process = None
		# self.killprocess = False
		# self.procout = None
		# self.procerr = None
		#self.useShell = False?
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
		# return (self.__dict__ == obj.__dict__)

	def runAndMonitor(self):
		""""""
		# self.process = procc.ProcessTimer(self)
		# self.process.start()

		process = procc.Process(self)
		process.start()
