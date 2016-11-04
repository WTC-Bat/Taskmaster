import os
import signal

def getSignalValue(sig):
	"""sig -> string or int, eg. 'SIGINT', '2', or 2"""
	for key, val in signal.__dict__.items():
		if (key.startswith("SIG")):
			if (isinstance(sig,(int, long)) == True):
				if (val == sig):
					return val
			elif (sig.isdigit() == True):
				if (val == int(sig)):
					return val
			else:
				if (key == sig):
					return val
	return (-42)


def isExecutable(filepath):
	"""
	Return True if the file specified in 'filepath' is executable. If not,
	False is returned
	"""
	if (os.path.isfile(filepath) and os.access(filepath, os.X_OK)):
		return (True)
	return (False)


def programAlreadyLoaded(programList, program):
	"""
	Returns True if 'programs' exists in 'programList'.
	Uses 'Program.progname' to determine equality
	"""
	for prog in programList:
		# if (prog == program):
		if (prog.progname == program.progname):
			return (True)
	return (False)


def programChanged(programList, program):
	"""
	If the 'program' exists in 'programList' but it's variables
	have changed, returns a Program object with the new variables.
	Programs existence is determined using the program's 'progname' element
	"""
	for prog in programList:
		if (prog.progname == program.progname):
			if not (prog == program):
				return (prog)
	return (None)


# def programChanged(programList, program):
# 	"""
# 	Returns true if the 'program' exists in 'programList' but it's variables
# 	have changed. Programs existence is determined using the program's
# 	'progname' element
# 	"""
# 	for prog in programList:
# 		if (prog.progname == program.progname):
# 			if not (prog == program):
# 				return (True)
# 	return (False)
