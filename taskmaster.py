#!/usr/bin/env python
import os
import cmd
import time
import signal
import platform
import threading
import tmdata
import tmfuncs
import process_class as procc
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
		if (len(self.programs) > 0):
			self.stopPrograms(["stop", "all"])
		log("TaskMaster exiting", "./tmlog.txt", False)
		exit(0)

	def default(self, line):
		'''Custom input handling'''
		log("Input: '" + line + "'", "./tmlog.txt", False)
		if (line.startswith("status")):
			self.showStatus(line.split())
		elif (line.startswith("stop")):	#this if statement is only if programs require a specific SIGNAL to stop
			self.stopPrograms(line.split())
		elif (line.startswith("start")):
			self.startPrograms(line.split())
		elif (line.startswith("restart")):
			self.restartPrograms(line.split())
		# elif (line == "-h" or line == "help"):
		# 	print("Help:")
		# elif (line == "clear"):	#tmp
		# 	for prog in self.programs:
		# 		prog.clearInactiveProcesses()
		else:
			log("Unknown command: " + line, "./tmlog.txt", True)

	def launchProgram(self, program):
		""""""
		cnt = 0
		num = 0
		totnum = 0

		log("Launching " + program.progname, "./tmlog.txt", False)
		while cnt < program.procnum:
			program.runAndMonitor()
			cnt += 1
		log(str(cnt) + " processes started from program " + program.progname,
			"./tmlog.txt", False)

	def restartPrograms(self, args):
		""""""
		cnt = 1
		found = False

		if (len(args) == 1):
			for prog in self.programs:
				if (len(prog.processes) > 0):
					for proc in prog.processes:
						# if (proc.active == True):
						if (proc.active == True and proc.pop.returncode == None):
						# if (proc.active == True and proc.started == True
						# 	and	proc.pop):
							# log("Restarting " + proc.name + "...",
							# 	"./tmlog.txt", False)
							proc.stop = True;
							signum = tmfuncs.getSignalValue(prog.stopsig)
							proc.pop.send_signal(signum)
							# proc.pop = None #?
						proc.run()
		elif (len(args) > 1):
			while cnt < len(args):
				for prog in self.programs:
					if (prog.progname == args[cnt]):
						found = True
						if (len(prog.processes) > 0):
							for proc in prog.processes:
								# if (proc.active == True):
								if (proc.active == True and proc.pop.returncode == None):
								# if (proc.active == True
								# 	and proc.started == True
								# 	and proc.pop):
									proc.stop = True
									signum = tmfuncs.getSignalValue(prog.stopsig)
									proc.pop.send_signal(signum)
									# proc.pop = None #?
								proc.run()
				if (found == False):
					log("No program '" + args[cnt] + "' in config",
						"./tmlog.txt", True)
				found = False
				cnt += 1

	def showStatus(self, args):
		""""""
		cnt = 1
		found = False
		stat = ""

		print("")
		if (len(args) == 1):
			for prog in self.programs:
				print(prog.progname + ":")
				if (len(prog.processes) > 0):
					for proc in prog.processes:
						if (proc.active == True):
							stat = "Active"
						else:
							stat = "Inactive"
						print(proc.name + " - " + stat)
					print("")
				else:
					print("Not launched\n")
		elif (len(args) > 1):
			while cnt < len(args):
				for prog in self.programs:
					if (prog.progname == args[cnt]):
						found = True
						print(prog.progname + ":")
						if (len(prog.processes) > 0):
							for proc in prog.processes:
								if (proc.active == True):
									stat = "Active"
								else:
									stat = "Inactive"
								print(proc.name + " - "	+ stat)
							print("")
						else:
							print("Not launched\n")
				if (found == False):
					log("No program '" + args[cnt] + "' in config",
						"./tmlog.txt", True)
				found = False
				cnt += 1

	def startPrograms(self, args):
		""""""
		cnt = 1
		found = False

		if (len(args) == 1):
			print ("Please specify which program\s to start."
					+ "\n(start all -OR- start [program1 name] "
					+ "[program2 name])")
		elif (len(args) > 1):
			if (args[1] == "all"):
				for prog in self.programs:
					if (len(prog.processes) > 0):
						for proc in prog.processes:
							if (proc.active == False):
								proc.run()
					else:
						self.launchProgram(prog)
			else:
				while cnt < len(args):
					for prog in self.programs:
						if (prog.progname == args[cnt]):
							found = True
							if (len(prog.processes) > 0):
								for proc in prog.processes:
									if (proc.active == False):
										proc.run()
							else:
								self.launchProgram(prog)
					if (found == False):
						log("No program '" + args[cnt] + "' in config",
							"./tmlog.txt", True)
					found = False
					cnt += 1

	def stopPrograms(self, args):
		""""""
		cnt = 1
		found = False

		if (len(args) == 1):
			print ("Please specify which program\s to stop."
					+ "\n(stop all -OR- stop [program1 name] "
					+ "[program2 name])")
		elif (len(args) > 1):
			if (args[1] == "all"):
				for prog in self.programs:
					if (len(prog.processes) > 0):
						for proc in prog.processes:
							if (proc.active == True):
							# if (proc.active == True and proc.pop):
							# if (proc.active == True and proc.pop.pid):
							# if (proc.active == True and proc.isAlive()):
							# if (proc.active == True and proc.pop.returncode == None):
								proc.stop = True
								signum = tmfuncs.getSignalValue(prog.stopsig)
								proc.pop.send_signal(signum)
								# proc.pop = None #?
			else:
				while cnt < len(args):
					for prog in self.programs:
						if (prog.progname == args[cnt]):
							found = True
							if (len(prog.processes) > 0):
								for proc in prog.processes:
									if (proc.active == True):
									# if (proc.active == True and proc.pop)
									# if (proc.active == True and proc.pop.pid):
									# if (proc.active == True and proc.isAlive()):
									# if (proc.active == True and proc.pop.returncode == None):
										proc.stop = True
										signum = tmfuncs.getSignalValue(
													prog.stopsig)
										proc.pop.send_signal(signum)
										# proc.pop = None #?
					if (found == False):
						log("No program '" + args[cnt] + "' in config",
							"./tmlog.txt", True)
					found = False
					cnt += 1

	def programsStarted(self):
		""""""
		for prog in self.programs:
			if (prog.active == False):
				return (False)
		return (True)


	def handleSigint(self, signum, frame):
		""""""
		if (signum == 2):
			print("")
			self.do_exit(None)


def autolaunchPrograms(taskmaster):
	""""""
	cnt = 0
	num = 0
	totnum = 0

	if (len(taskmaster.programs) == 0):
		log("WARNING: No programs in config file", "./tmlog.txt", True)
		return
	for program in taskmaster.programs:
		if (program.autolaunch == True):
			while num < program.procnum:
				program.runAndMonitor()
				num += 1
			totnum += num
			num = 0
			cnt += 1
			log("Starting " + program.progname, "./tmlog.txt", True)
			# while taskmaster.programsStarted == False:
			log(program.progname + " started!", "./tmlog.txt" , True)
	if (cnt > 0):
		log(str(totnum) + " processes (" + str(cnt) + " program\s) launched"
			+ " automatically",	"./tmlog.txt", True)
	else:
		log("No programs set to launch automatically", "./tmlog.txt", True)


def clearLog():
	""""""
	if (os.path.getsize("./tmlog.txt") > 0):
		log = open("./tmlog.txt", "w")
		log.close()


def main():
	""""""
	tm = Taskmaster()

	clearLog()
	log("TaskMaster started", "./tmlog.txt", False)
	print("Loading programs")
	if str(platform.system()) != "Windows":
		os.system("clear")
	else:
		os.system("cls")
	log("Loading config file", "./tmlog.txt", False)
	tm.programs = tmdata.loadConfig(os.path.realpath("./config.xml"))
	log(str(len(tm.programs)) + " programs loaded from config", "./tmlog.txt",
		False)
	autolaunchPrograms(tm)
	signal.signal(signal.SIGINT, tm.handleSigint)#!#
	tm.cmdloop()


if __name__ == "__main__":
	main()
