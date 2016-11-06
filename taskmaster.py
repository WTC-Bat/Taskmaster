#!/usr/bin/env python
import os
import tmdata
from taskmaster_class import Taskmaster
from tmlog import log


def autolaunchPrograms(taskmaster):
	""""""
	cnt = 0
	totnum = 0

	if (len(taskmaster.programs) == 0):
		log("WARNING: No programs in config file", "./tmlog.txt", True)
		return
	for program in taskmaster.programs:
		if (program.autolaunch == True):
			log("Starting " + program.progname, "./tmlog.txt", False)
			totnum += program.runAndMonitor()
			cnt += 1
	if (cnt > 0):
		print("Taskmaster is starting autolaunch programs. Please wait...")
		while taskmaster.programsWaiting() == True:
			continue
		log(str(totnum) + " processes (" + str(cnt) + " program\s) successfully"
			+ " launched",	"./tmlog.txt", True)
	else:
		log("No programs set to launch automatically", "./tmlog.txt", True)


def clearLog():
	""""""
	if (os.path.exists("./tmlog.txt")):
		if (os.path.getsize("./tmlog.txt") > 0):
			log = open("./tmlog.txt", "w")
			log.close()


def main():
	"""
	NOTE: Nothing printed here will be visible as cmdloop clears the screen
	"""
	tm = Taskmaster()

	clearLog()
	log("TaskMaster started", "./tmlog.txt", False)
	os.system("clear")
	log("Loading config file", "./tmlog.txt", False)
	tm.programs = tmdata.loadConfig("./config.xml")
	log(str(len(tm.programs)) + " programs loaded from config", "./tmlog.txt",
		False)
	autolaunchPrograms(tm)
	tm.cmdloop()


if __name__ == "__main__":
	main()
