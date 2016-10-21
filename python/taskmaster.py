#!/usr/bin/env python
import os
import cmd
import platform
import sched
import tmdata
import threading

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
		self.programs = list()
		self.procs = list()	#?

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
		return -1

	def default(self, line):
		'''Custom input handling'''
		if (line == "cheese"):
			print "Crackers"
		elif line == "load":
			self.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
			print("\n---Programs Loaded---\n")
		elif line == "sched":
			if not self.programs:
				print("Load config first!")
				return
		# elif line.startswith("sched"):
		# 	sc = line.split()
		# 	if count(sc) == 1:
		# 		testsched()
		# 		print("\n---Monitoring " + str(len(self.programs))
		# 				+ " programs---\n")
		# 		self.testsched()
		# 	else:
			print("\n---Monitoring " + str(len(self.programs))
					+ " programs---\n")
			self.testsched()
		else:
			print("Unknown command")


	def testsched(self):
		""""""
		#
		#	initialtests
		#




		# for program in self.programs:
		# 	self.procs.append(program.runAndMonitor())


		# print("testsched")
		# tim = threading.Timer(5, self.testsched)
		# tim.start()

		# program.runAndMonitor()
		#
		#	initialtests
		#


def main():
	""""""
	tm = Taskmaster()
	if str(platform.system()) != "Windows":
		os.system("clear")
	else:
		os.system("cls")
	tm.cmdloop()


if __name__ == "__main__":
	main()
