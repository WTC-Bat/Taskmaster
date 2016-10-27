#!/usr/bin/env python
import os
import cmd
import platform
import sched
import tmdata
import threading
import process_class as procc
import time
from tmlog import log

#	subprocess

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
		exit(0)

	def default(self, line):
		'''Custom input handling'''
		if (line == "cheese"):
			print "Crackers"
		# elif line == "load":
		# 	self.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
		# 	print("\n---Programs Loaded---\n")
		elif line.startswith("monitor"):
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
						program.runAndMonitor()
						print("\n---Monitoring " + program.progname + " ---\n")
				#check if progname is in config and if not notify user!!!
		# elif (line == "log"):
		# 	#?#Untested#?#
		# 	log(time.ctime() + "\tTEST LOG!", "./log.txt")
		# 	log(time.ctime() + "\tTEST LOG END!", "./log.txt")
		else:
			print("Unknown command")


def autolaunchPrograms(taskmaster):
	""""""
	cnt = 0
	for program in taskmaster.programs:
		if (program.autolaunch == True):
			program.runAndMonitor()
			cnt += 1
	print(str(cnt) + " programs launched automatically")


def main():
	""""""
	tm = Taskmaster()
	if str(platform.system()) != "Windows":
		os.system("clear")
	else:
		os.system("cls")
	tm.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
	if (len(tm.programs) > 0):
		print("\n---Programs Loaded---\n")
	autolaunchPrograms(tm)
	tm.cmdloop()


if __name__ == "__main__":
	main()
