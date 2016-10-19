import array

class Program():
	""""""
	# command = ""
	# procnum = 1
	# autolaunch = True
	# starttime = 5
	# restart = "unexpected"
	# retries = 3
	# stopsig = ""
	# stoptime = 10
	# exitcodes = list()
	# exitcodes = None
	# stdout = ""
	# stderr = ""
	# redir = ""
	# envvars = dict()
	# workingdir = ""
	# umask = ""

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
