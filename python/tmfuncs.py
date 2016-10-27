import signal


def registerSignals(programs):
	""""""
	print("RS")


def getSignalValue(sig):
	"""sig -> string or int, eg. 'SIGINT', '2', or 2"""
	for key, val in signal.__dict__.items():
		if (key.startswith("SIG")):
			if (isinstance(sig,(int, long)) == True):
				if (val == sig):
					return val
			elif (sig.isnumeric() == True):
				if (val == int(sig)):
					return val
			else:
				if (key == sig):
					return val
	return (-42)
