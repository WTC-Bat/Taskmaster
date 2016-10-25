import os

def log(message, logfile):
	""""""
	path = os.path.join(os.path.dirname(__file__), logfile)
	if not (os.path.exists(logfile)):
		f = open(path, "w")
		f.close()
	with open(path, "a") as log:
		log.write(message + "\n")
