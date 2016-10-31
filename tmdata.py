import os
import re
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import tmfuncs
from tmlog import log
from program_class import Program


def checkProgramCommand(program):
	""""""
	cmd = ""
	path = ""
	for pth in os.environ["PATH"].split(os.pathsep):
		cmd = program.command.split()
		path = os.path.join(pth, cmd[0])
		if (tmfuncs.isExecutable(cmd[0]) or tmfuncs.isExecutable(path)):
			return (True)
	return (False)


def cleanConfig(config):
	"""Removes all the empty lines from the config file."""
	path = os.path.join(os.path.dirname(__file__), config)
	s = ""

	with open(path, "r") as f:
		for line in f:
			if not re.match(r"^\s*$", line):
				s+=line
	with open(path, "w") as f:
		f.write(s)


def loadConfig(config):
	"""Returns a 'list()' of 'Programs' from the xml config file"""
	path = os.path.join(os.path.dirname(__file__), config)
	prog = None
	progs = list()
	xdoc = None

	if os.path.exists(path) and os.path.getsize(path) != 0:
		prog = Program()
		xdoc = ET.parse(path)
		xroot = xdoc.getroot()
		for xprog in xroot:
			prog = programFromElement(xprog)
			if (checkProgramCommand(prog) == True):
				progs.append(prog)
			else:
				log("'" + prog.progname + "' command invalid. Not loading",
					"./tmlog.txt", True)
			# progs.append(prog)
	return (progs)


def programExists(program, config):
	"""Checks if the 'Program' object exists in the xml config file"""
	path = os.path.join(os.path.dirname(__file__), config)
	prog = None
	xdoc = None

	if os.path.exists(path) and os.path.getsize(path) > 0:
		xdoc = ET.parse(path)
		xroot = xdoc.getroot()
		for xprog in xroot:
			prog = programFromElement(xprog)
			if prog == program:
				return (True)
	return (False)


def programFromElement(progel):
	"""Returns a 'Program' object from a 'Program XML Element'"""
	prog = Program()
	codes = list()
	evars = dict()

	for el in progel:
		if el.tag == "progname":
			prog.progname = el.text
		elif el.tag == "command":
			prog.command = el.text
		elif el.tag == "procnum":
			prog.procnum = int(el.text)
		elif el.tag == "autolaunch":
			prog.autolaunch = el.text
		elif el.tag == "starttime":
			prog.starttime = int(el.text)
		elif el.tag == "restart":
			prog.restart = el.text
		elif el.tag == "retries":
			prog.retries = int(el.text)
		elif el.tag == "stopsig":
			prog.stopsig = el.text
		elif el.tag == "stoptime":
			prog.stoptime = int(el.text)
		elif el.tag == "exitcodes":
			for chel in el:
				codes.append(int(chel.text))
			prog.exitcodes = codes
		elif el.tag == "stdout":
			prog.stdout = el.text
		elif el.tag == "stderr":
			prog.stderr = el.text
		elif el.tag == "redout":
			if (el.text == "True"):
				prog.redout = True
			else:
				prog.redout = False
			# prog.redout = bool(el.text)
		elif el.tag == "rederr":
			if (el.text == "True"):
				prog.rederr = True
			else:
				prog.rederr = False
			# prog.rederr = bool(el.text)
		# elif el.tag == "redout":
		# 	prog.redout = el.text
		# elif el.tag == "rederr":
		# 	prog.rederr = el.text
		elif el.tag == "envvars":
			var = None
			val = None
			for chel in el:
				for chch in chel:
					if chch.tag == "var":
						var = chch.text
					elif chch.tag == "val":
						val = chch.text
				evars[var] = val
			prog.envvars = evars
		elif el.tag == "workingdir":
			prog.workingdir = el.text
		elif el.tag == "umask":
			prog.umask = el.text
	# print("redout - " + prog.progname + " - " + str(prog.redout))
	# print("rederr - " + prog.progname + " - " + str(prog.rederr))
	return (prog)


def removeProgam(program, config):
	"""Removes the specified 'Program' from the xml config file"""
	path = os.path.join(os.path.dirname(__file__), config)
	prog = None

	if os.path.exists(path) and os.path.getsize(path) > 0:
		xdoc = ET.parse(path)
		xroot = xdoc.getroot()
		for xprog in xroot:
			prog = programFromElement(xprog)
			if prog == program:
				xroot.remove(xprog)
				xdoc.write(path, encoding="utf-8", xml_declaration=True)
				return



def saveProgram(program, config, overwrite):
	"""
	Saves a single 'program' object to the xml file specified in 'config'. If
	the	program already exists in the file and 'overwrite' is true, the program
	entry in the xml file will be removed and re-written
	"""
	path = None
	f = None
	xdoc = None
	xroot = None
	xel = None

	#	if two programs with the same command are not allowed, then we just
	#	need to check if two objects have the same command. At the moment,
	#	two objects will only be equal if all members are the same. Moreover,
	#	this also renders replacing program entries pointless
	if programExists(program, config):
		if overwrite == False:
			return
		## else:
			## replace xml entry
			## return
	path = os.path.join(os.path.dirname(__file__), config)
	if not os.path.exists(path):
		f = open(path, "w")
		f.close()
	if os.path.getsize(path) == 0:
		xdoc = MD.Document()
		xroot = xdoc.createElement("Programs")
		xdoc.appendChild(xroot)
	else:
		xdoc = MD.parse(path)
		xroot = xdoc.documentElement
	xprog = xdoc.createElement("Program")
	for key, val in vars(program).iteritems():
		if type(val) is list and key == "exitcodes":
			 xel = xdoc.createElement("exitcodes")
			 for i in val:
				 xcode = xdoc.createElement("code")
				 xcode.appendChild(xdoc.createTextNode(str(i)))
				 xel.appendChild(xcode)
		elif key == "envvars" and type(val) is dict:
			xel = xdoc.createElement("envvars")
			for k, v in val.iteritems():
				xenv = xdoc.createElement("envvar")
				xvar = xdoc.createElement("var")
				xval = xdoc.createElement("val")
				xvar.appendChild(xdoc.createTextNode(k))
				xval.appendChild(xdoc.createTextNode(v))
				xenv.appendChild(xvar)
				xenv.appendChild(xval)
				xel.appendChild(xenv)
		else:
			xel = xdoc.createElement(key)
			xel.appendChild(xdoc.createTextNode(str(val)))
		xprog.appendChild(xel)
	xroot.appendChild(xprog)
	with open(path, "w") as xml:
		xml.write(xdoc.toprettyxml(indent="\t", encoding="utf-8"))
	cleanConfig(config)
