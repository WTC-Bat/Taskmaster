import cmd
import signal
import tmdata
import tmfuncs
from tmlog import log

class Taskmaster(cmd.Cmd):
	"""Main program class. Handles input and cmdloop"""
	def __init__(self):
		"""'Taskmaster' constructor"""
		cmd.Cmd.__init__(self)
		self.prompt = "\033[94mTaskmaster>\033[0m "
		self.programs = list()
		signal.signal(signal.SIGINT, self.handleSigint)
		signal.signal(signal.SIGHUP, self.handleSighup)
		# log("Taskmaster object initialized", "./tmlog.txt", False)

	def emptyline(self):
		"""If the input line is empty, continue and show prompt"""
		pass

	def do_help(self, args):
		"""Display Taskmaster help and commands"""
		print("-h:")
		print("help:\n\tshow these commands")
		print("programs:\n\tprint a list of loaded programs\n")
		print("reload:\n\treload config file new/changed "
				+ "programs\n")
		print("restart:\n\trestart all programs, active or inactive\n")
		print("restart [progName1] [progName2] [...]:\n\trestart programs "
				+ "'progName1' and 'progName2', active or inactive\n")
		print("status:\n\tshow the status of all loaded programs\n")
		print("start [progName1] [progName] [...]:\n\tstart programs "
				+ "'progName1' and 'progName2' if they are inactive\n")
		print("start all:\n\tstart all inactive programs\n")
		print("stop [progName1] [progName2] [...]:\n\tstop programs 'progName1'"
				+ " and 'progName2' if they are active\n")
		print("stop all:\n\tstop all active programs\n")

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
		elif (line == "reload"):
			self.reloadConfig()
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

	def reloadConfig(self):
		""""""
		cnt = 0
		rmcnt = 0
		chcnt = 0
		chprogs = list()
		allnewprogs = list()
		toremove = list()
		allconfig = tmdata.loadConfig("./config.xml")
		newprogs = tmdata.loadNewPrograms("./config.xml", self.programs)
		stopstring = "stop"
		startstring = "start"

		# removes all programs from 'self.programs' that are no longer present
		# in the config file
		for prog in self.programs:
			if (tmdata.programExists(prog, "./config.xml") == False):
				rmcnt += 1
				toremove.append(prog)
				# log("'" + prog.progname + "' no longer in config, removing",
				# 	"./tmlog.txt", False)

		# this loop checks if a program's variables have changed, and if so,
		# adds a new Program with changed variables to 'chprogs'
		for prog in self.programs:
			chprog = tmfuncs.programChanged(allconfig, prog)
			if not (chprog == None):
				chcnt += 1
				toremove.append(prog)
				chprogs.append(chprog)
				# log("'" + prog.progname + "' has changed variables, reloading",
				# 	"./tmlog.txt", False)

		# ensure some sort of change ocurred
		if (rmcnt == 0 and chcnt == 0 and len(newprogs) == 0):
			print("No changes to config.")
			return

		# log the change\s
		if (len(newprogs) > 0):
			log(str(len(newprogs)) + " new programs added to config",
				"./tmlog.txt", True)
		if (chcnt > 0):
			log(str(chcnt) + " programs changed in config", "./tmlog.txt", True)
		if (rmcnt > 0):
			log(str(rmcnt) + " programs removed from config", "./tmlog.txt",
				True)

		# stop programs in 'self.programs' that exist in 'toremove'
		for prog in self.programs:
			for rprog in toremove:
				# if (rprog == prog):
				if (rprog.progname == prog.progname):
					if (prog.hasActiveProcesses() == True):
						cnt += 1
						stopstring += " " + prog.progname

		# stop runnuing processes
		print("Reloading config file...")
		if (cnt > 0):
			self.default(stopstring)
			self.waitForPrograms()
		cnt = 0

		# remove programs in 'self.programs' that exist in 'toremove'
		for rprog in toremove:
			for prog in self.programs:
				if (prog.progname == rprog.progname):
					self.programs.remove(prog)

		# adds all changed programs to 'allnewprogs'
		for prog in chprogs:
			allnewprogs.append(prog)

		# adds all new programs to 'allnewprogs'
		for prog in newprogs:
			allnewprogs.append(prog)

		# adds programs from 'allnewprogs' to 'self.programs' and starts them
		# if applicable
		for prog in allnewprogs:
			self.programs.append(prog)
			if (prog.autolaunch == True):
				startstring += " " + prog.progname
				cnt += 1
		if (cnt > 0):
			self.default(startstring)
			self.waitForPrograms()


	def restartPrograms(self, args):
		""""""
		cnt = 1
		num = 0
		procs = 0
		found = False

		if (len(args) == 1):
			num = len(self.programs)
			for prog in self.programs:
				if (len(prog.processes) > 0):
					procs += len(prog.processes)
					for proc in prog.processes:
						if (proc.active == True and proc.pop.returncode == None):
							proc.stop = True;
							signum = tmfuncs.getSignalValue(prog.stopsig)
							proc.pop.send_signal(signum)
							# proc.pop = None #?
						proc.timetostart = 0
						proc.run()
		elif (len(args) > 1):
			while cnt < len(args):
				for prog in self.programs:
					if (prog.progname == args[cnt]):
						found = True
						num += 1
						if (len(prog.processes) > 0):
							procs += len(prog.processes)
							for proc in prog.processes:
								if (proc.active == True and proc.pop.returncode == None):
									proc.stop = True
									signum = tmfuncs.getSignalValue(prog.stopsig)
									proc.pop.send_signal(signum)
									# proc.pop = None #?
								proc.timetostart = 0
								proc.run()
				if (found == False):
					log("No program '" + args[cnt] + "' in config",
						"./tmlog.txt", True)
				found = False
				cnt += 1
		if (self.programsWaiting() == True):
			log("Restarting " + str(num) + " programs", "./tmlog.txt", False)
			print("Restarting " + str(num) + " programs. Please wait...")
			self.waitForPrograms()
			log(str(procs) + " processes restarted", "./tmlog.txt", True)

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
								proc.timetostart = 0
								proc.run()
					else:	# for programs not yet launched
						procs += prog.runAndMonitor()
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
										proc.timetostart = 0
										proc.run()
							else:
								procs += prog.runAndMonitor()
					if (found == False):
						log("No program '" + args[cnt] + "' in config",
							"./tmlog.txt", True)
					found = False
					cnt += 1
		if (num > 0):
			log("Starting " + str(num) + " progam\s", "./tmlog.txt", False)
			print("Starting " + str(num) + " program\s. Please wait...")
			self.waitForPrograms()
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
							# if (proc.active == True):
							if (proc.active == True and proc.pop.returncode == None):
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
									# if (proc.active == True):
									if (proc.active == True and proc.pop.returncode == None):
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
				self.waitForPrograms()
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

	def handleSighup(self, signum, frame):
		""""""
		if (signum == signal.SIGHUP):
			log("Reloading config file", "./tmlog.txt", False)
			self.reloadConfig()

	def handleSigint(self, signum, frame):
		""""""
		if (signum == 2):
			print("")
			self.do_exit(None)

	def waitForPrograms(self):
		while self.programsWaiting() == True:
			continue
