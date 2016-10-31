import os
import time

def log(message, logfile, toprint):
	"""	message - the message to display
		logfile - file to write to
		toprint - True to also print the message
	"""
	path = os.path.join(os.path.dirname(__file__), logfile)
	txt = time.ctime() + "\t" + message
	with open(path, "a") as log:
		log.write(txt + "\n")
	if (toprint == True):
		print(message)
