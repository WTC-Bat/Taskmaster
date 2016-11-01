import os
import time

def log(message, logfile, toprint):
	"""	message - the message to display
		logfile - file to write to
		toprint - True to also print the message
	"""
	path = os.path.join(os.path.dirname(__file__), logfile)
	txt = time.ctime() + "\t" + message
	if (os.path.getsize(path) >= 2000000):
		log = open(path, "w")
	else:
		log = open(path, "a")
	log.write(txt + "\n")
	log.close()
	if (toprint == True):
		print(message)
