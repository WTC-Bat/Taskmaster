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

# def testFileSize(file):
# 	""""""
# 	return ()
