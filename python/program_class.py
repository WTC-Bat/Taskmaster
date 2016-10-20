import array

class Program():
	""""""
	def __init__(self, args=None):
		""""""
		if type(args) is dict:
			for key, val in args.iteritems():
				if key == "command":
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
				elif key == "redir":
					self.redir = val
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
		return (("command: {}\nprocnum: {}\nautolaunch: {}\nstarttime: {}\n"
				"restart: {}\nretries: {}\nstopsig: {}\nstoptime: {}\n"
				"exitcodes: {}\nstdout: {}\nstderr: {}\nredir: {}\n"
				"envvars: {}\nworkingdir: {}\numask: {}\n"))\
				.format(self.command, self.procnum, self.autolaunch,
						self.starttime, self.restart, self.retries,
						self.stopsig, self.stoptime, self.exitcodes,
						self.stdout, self.stderr, self.redir, self.envvars,
						self.workingdir, self.umask)

	def __eq__(self, obj):
		""""""
		return (str(self) == str(obj))
		# return (self.__dict__ == obj.__dict__)
