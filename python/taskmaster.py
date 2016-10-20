#!/usr/bin/env python
import os
import cmd
import platform


class Taskmaster(cmd.Cmd):
	""""""
	def __init__(self):
		""""""
		cmd.Cmd.__init__(self)
		if str(platform.system()) != "Windows":
			self.prompt = "\033[94mTaskmaster>\033[0m "
		else:
			self.prompt = "Taskmaster> "
		# self.prompt = "\033[94mTaskmaster>\033[0m "
		# self.prompt = "Taskmaster> "

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


def main():
	""""""
	tm = Taskmaster()
	os.system("clear")
	# if str(platform.system()) != "Windows":
	# 	tm.prompt = "\033[94mTaskmaster>\033[0m "
	# else:
	# 	tm.prompt = "Taskmaster> "
	tm.cmdloop()


if __name__ == "__main__":
	main()
