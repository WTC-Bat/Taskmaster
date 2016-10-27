#!/usr/bin/env python
import os
import cmd
import time
import platform
import tmdata
import process_class as procc
# import tmmsg
from tmlog import log

class Taskmaster(cmd.Cmd):
	""""""
	def __init__(self):
		""""""
		cmd.Cmd.__init__(self)
		if str(platform.system()) != "Windows":
			self.prompt = "\033[94mTaskmaster>\033[0m "
		else:
			self.prompt = "Taskmaster> "
		self.programs = list
		# self.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
		# if (len(self.programs) > 0):
		# 	print("\n---Programs Loaded---\n")
		# self.autolaunchPrograms()?
		log("Taskmaster object initialized", "./tmlog.txt", False)

	def emptyline(self):
		""""""
		pass

	def do_hist(self, args):
		""""""
		print self._hist

	"""
	def preloop(self):
		""""""
	"""

	"""
	def postloop(self):
		""""""
	"""

	def do_exit(self, args):
		'''Exits the Taskmaster shell when user inputs "exit"'''
		if (len(self.programs) != 0):
			for program in self.programs:
				if (program.process != None):
					program.process.killprocess = True
		log("TaskMaster exiting", "./tmlog.txt", False)
		exit(0)

	def default(self, line):
		'''Custom input handling'''
		log("Input: '" + line + "'", "./tmlog.txt", False)
		if (line == "cheese"):				###
			print "Crackers"
		elif line == "load":				###
			self.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
			print("\n---Programs Loaded---\n")
		elif line.startswith("monitor"):	###
			if not self.programs:
				print("Load config first!")
				return
			sc = line.split()
			if len(sc) == 1:
				for program in self.programs:
					program.runAndMonitor()
				print("\n---Monitoring " + str(len(self.programs))
						+ " programs---\n")
			else:
				for program in self.programs:
					if program.progname == sc[1]:
						print("\n---Monitoring " + program.progname + " ---\n")
						program.runAndMonitor()
				#check if progname is in config and if not notify user!!!
		elif line == "dlog":
			os.remove("./tmlog.txt")
			print("./tmlog.txt deleted!")
		#----------------------------------------------------------------#
		elif (line.startswith("status")):
			print("ALL STATUS")
			# splt = line.split()
			# if (len(splt) == 1):
			# log("Showing status ")	???
			# 	showstatus()
		elif (line.startswith("stop")):
			print("STOP")
		elif (line.startswith("start")):
			print("START")
		else:
			log("Unknown command: " + line, "./tmlog.txt", True)


def autolaunchPrograms(taskmaster):
	""""""
	cnt = 0

	if (len(taskmaster.programs) == 0):
		log("WARNING: No programs in config file", "./tmlog.txt", True)
		return
	for program in taskmaster.programs:
		if (program.autolaunch == True):
			program.runAndMonitor()
			cnt += 1
	if (cnt > 0):
		log(str(cnt) + " programs launched automatically", "./tmlog.txt", True)
	else:
		log("No programs set to launch automatically", "./tmlog.txt", True)


def main():
	""""""
	log("TaskMaster started", "./tmlog.txt", False)
	tm = Taskmaster()

	if str(platform.system()) != "Windows":
		os.system("clear")
	else:
		os.system("cls")
	log("Loading config file", "./tmlog.txt", False)
	tm.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
	log("Config file successfully loaded", "./tmlog.txt", False)
	# autolaunchPrograms(tm)
	tm.cmdloop()


if __name__ == "__main__":
	main()
