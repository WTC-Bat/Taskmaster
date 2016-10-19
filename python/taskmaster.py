#!/usr/bin/env python
import os
import cmd


class Taskmaster(cmd.Cmd):
	""""""
	def __init__(self):
		""""""
		cmd.Cmd.__init__(self)
		self.prompt = "\033[94mTaskmaster>\033[0m "

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
		elif (line == "init"):
			print "init";


if __name__ == "__main__":
	tm = Taskmaster()
	os.system("clear")
	tm.cmdloop()
