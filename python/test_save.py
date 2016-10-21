#!/usr/bin/env python
from program_class import Program
import tmdata
import os

def main():
	""""""
	args1 = {"command" : "/usr/bin/whoami",
			"procnum" : 1,
			"autolaunch" : True,
			"starttime" : 5,
			"restart" : "never",
			"retries" : 2,
			"stopsig" : "SSIG",
			"stoptime" : 10,
			"exitcodes" : [0, 2, 4, 5],
			"stdout" : "/usr/bin/whoami.stdout",
			"stderr" : "/usr/bin/whoami.stderr",
			"redir" : "/usr/bin/whoami.redir",
			"envvars" : {"ENV1" : "VAL1", "ENV2" : "VAL2"},
			"workingdir" : "/tmp",
			"umask" : "077"}

	args2 = {"command" : "/usr/bin/whois",
			"procnum" : 1,
			"autolaunch" : True,
			"starttime" : 5,
			"restart" : "never",
			"retries" : 2,
			"stopsig" : "SSIG",
			"stoptime" : 10,
			"exitcodes" : [0, 2, 4, 5],
			"stdout" : "/usr/bin/whois.stdout",
			"stderr" : "/usr/bin/whois.stderr",
			"redir" : "/usr/bin/whois.redir",
			"envvars" : {"ENV1" : "VAL1", "ENV2" : "VAL2"},
			"workingdir" : "/tmp",
			"umask" : "077"}

	# args1 = {"command" : "/C/Downloads/darkradiant-1.8.0-x64",
	# 		"procnum" : 1,
	# 		"autolaunch" : True,
	# 		"starttime" : 5,
	# 		"restart" : "never",
	# 		"retries" : 2,
	# 		"stopsig" : "SSIG",
	# 		"stoptime" : 10,
	# 		"exitcodes" : [0, 2, 4, 5],
	# 		"stdout" : "/C/Downloads/darkradiant-1.8.0-x64.stdout",
	# 		"stderr" : "/C/Downloads/darkradiant-1.8.0-x64.stderr",
	# 		"redir" : "/C/Downloads/darkradiant-1.8.0-x64.redir",
	# 		"envvars" : {"ENV1" : "VAL1", "ENV2" : "VAL2"},
	# 		"workingdir" : "/tmp",
	# 		"umask" : "077"}
	#
	# args2 = {"command" : "/C/UsbFix/UsbFix.exe",
	# 		"procnum" : 1,
	# 		"autolaunch" : True,
	# 		"starttime" : 5,
	# 		"restart" : "never",
	# 		"retries" : 2,
	# 		"stopsig" : "SSIG",
	# 		"stoptime" : 10,
	# 		"exitcodes" : [0, 2, 4, 5],
	# 		"stdout" : "/C/UsbFix/UsbFix.exe.stdout",
	# 		"stderr" : "/C/UsbFix/UsbFix.exe.stderr",
	# 		"redir" : "/C/UsbFix/UsbFix.exe.redir",
	# 		"envvars" : {"ENV1" : "VAL1", "ENV2" : "VAL2"},
	# 		"workingdir" : "/tmp",
	# 		"umask" : "077"}

	prog1 = Program(args1)
	prog2 = Program(args2)

	tmdata.saveProgram(prog1, "./config.xml", False)
	tmdata.saveProgram(prog2, "./config.xml", False)
	# tmdata.saveProgram(prog1, "./config.json", False)
	# tmdata.saveProgram(prog2, "./config.json", False)

if __name__ == "__main__":
	main();
