import cmd
import tmfuncs
from tmlog import log

class Taskmaster(cmd.Cmd):
	""""""
	def __init__(self):
		""""""
		cmd.Cmd.__init__(self)
		self.prompt = "\033[94mTaskmaster>\033[0m "
		self.programs = list
		log("Taskmaster object initialized", "./tmlog.txt", False)

	def emptyline(self):
		""""""
		pass

	def do_help(self, args):
		""""""
		print("Help:")

	def do_exit(self, args):
		'''Exits the Taskmaster shell when user inputs "exit"'''
		if (len(self.programs) > 0):
			self.stopPrograms(["stop", "all"])
		log("TaskMaster exiting", "./tmlog.txt", True)
		exit(0)

	def default(self, line):
		'''Custom input handling'''
		log("Input: '" + line + "'", "./tmlog.txt", False)
		if (line.startswith("status")):
			if (len(self.programs) < 1):
				print("No programs")
				return
			self.showStatus(line.split())
		elif (line.startswith("stop")):	#this if statement is only if programs require a specific SIGNAL to stop
			if (len(self.programs) < 1):
				print("No programs")
				return
			self.stopPrograms(line.split())
		elif (line.startswith("start")):
			if (len(self.programs) < 1):
				print("No programs")
				return
			self.startPrograms(line.split())
		elif (line.startswith("restart")):
			if (len(self.programs) < 1):
				print("No programs")
				return
			self.restartPrograms(line.split())
#------------------------------------------------------------------------------#
		elif (line == "-h"):
			self.do_help(None)
		elif (line.startswith("programs")):
			if (len(self.programs) < 1):
				print("No programs")
				return
			for prog in self.programs:
				print(prog)
		else:
			log("Unknown command: " + line, "./tmlog.txt", True)

	def activePrograms(self):
		"""Return the amount of programs with active processes"""
		cnt = 0

		for prog in self.programs:
			if (len(prog.processes) > 0):
				for proc in prog.processes:
					if (proc.active == True):
						cnt += 1
						break
		return (cnt)

	def allProgramsActive(self):
		""""""
		for prog in self.programs:
			if (len(prog.processes) > 0):
				for proc in prog.processes:
					if (proc.active == False):
						return (False)
			else:
				return (False)
		return (True)

	def restartPrograms(self, args):
		""""""
		cnt = 1
		num = 0
		found = False

		if (len(args) == 1):
			num = len(self.programs)
			for prog in self.programs:
				if (len(prog.processes) > 0):
					for proc in prog.processes:
						if (proc.active == True and proc.pop.returncode == None):
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
						num += 1
						if (len(prog.processes) > 0):
							for proc in prog.processes:
								if (proc.active == True and proc.pop.returncode == None):
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
		if (self.programsWaiting() == True):
			log("Restarting " + str(num) + " programs", "./tmlog.txt", False)
			print("\nRestarting " + str(num) + " programs. Please wait...\n")
			while self.programsWaiting() == True:
				continue

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
		num = 0
		procs = 0
		found = False

		if (len(args) == 1):
			print ("Please specify which program\s to start."
					+ "\n(start all -OR- start [program1 name] "
					+ "[program2 name])")
		elif (len(args) > 1):
			if (args[1] == "all"):
				if (self.allProgramsActive() == True):
					print("All programs already active. Use 'restart' to"
							+ " restart all programs")
					return
				num = (len(self.programs)) - (self.activePrograms())
				for prog in self.programs:
					if (len(prog.processes) > 0):
						for proc in prog.processes:
							if (proc.active == False):
								procs += 1
								proc.run()
					else:
						procs = prog.runAndMonitor()
			else:
				while cnt < len(args):
					for prog in self.programs:
						if (prog.progname == args[cnt]):
							found = True
							if (prog.hasInactiveProcesses() == False
									and len(prog.processes) > 0):
								print("Program '" + prog.progname
										+ "' already started")
								break
							num += 1
							if (len(prog.processes) > 0):
								for proc in prog.processes:
									if (proc.active == False):
										procs += 1
										proc.run()
							else:
								procs = prog.runAndMonitor()
					if (found == False):
						log("No program '" + args[cnt] + "' in config",
							"./tmlog.txt", True)
					found = False
					cnt += 1
		if (num > 0):
			log("Starting " + str(num) + " progam\s", "./tmlog.txt", False)
			print("Starting " + str(num) + " program\s. Please wait...")
			while self.programsWaiting() == True:
				continue
			print(str(procs) + " process\es started")

	def stopPrograms(self, args):
		""""""
		cnt = 1
		num = 0
		procs = 0
		found = False

		if (len(args) == 1):
			print ("Please specify which program\s to stop."
					+ "\n(stop all -OR- stop [program1 name] "
					+ "[program2 name])")
		elif (len(args) > 1):
			if (args[1] == "all"):
				num = self.activePrograms()
				if (num == 0):
					print("All programs already stopped")
					return
				for prog in self.programs:
					if (len(prog.processes) > 0):
						for proc in prog.processes:
							if (proc.active == True):
								proc.stop = True
								proc.stopping = True
								signum = tmfuncs.getSignalValue(prog.stopsig)
								proc.pop.send_signal(signum)
								procs += 1
			else:
				while cnt < len(args):
					for prog in self.programs:
						if (prog.progname == args[cnt]):
							found = True
							if (prog.hasActiveProcesses() == False):
								print("Program '" + prog.progname
										+ "' already stopped")
								break
							num += 1
							if (len(prog.processes) > 0):
								for proc in prog.processes:
									if (proc.active == True):
										proc.stop = True
										proc.stopping = True
										signum = tmfuncs.getSignalValue(
													prog.stopsig)
										proc.pop.send_signal(signum)
										procs += 1
					if (found == False):
						log("No program '" + args[cnt] + "' in config",
							"./tmlog.txt", True)
					found = False
					cnt += 1
			if (num > 0):
				print("Stopping " + str(num) + " program\s. Please wait...")
				while self.programsWaiting() == True:
					continue
				print(str(procs) + " process\es stopped.")
			num = 0

	def programsWaiting(self):
		""""""
		for prog in self.programs:
			if (len(prog.processes) > 0):
				for proc in prog.processes:
					if ((proc.starting == True) or (proc.stopping == True)):
						return (True)
		return (False)

	def handleSigint(self, signum, frame):
		""""""
		if (signum == 2):
			print("")
			self.do_exit(None)
