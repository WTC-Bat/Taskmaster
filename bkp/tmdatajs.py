import os
import json
from program_class import Program

# def programExists(program, config):
# 	""""""

def programFromElement(jsonobj):
	""""""
	prog = Program()

	for key, val in jsonobj.iteritems():
		if key == "command":
			prog.command = val
		elif key == "procnum":
			prog.procnum = val
		elif key == "autolaunch":
			prog.autolaunch = val
		elif key == "starttime":
			prog.starttime = int(val)
		elif key == "restart":
			prog.restart = val
		elif key == "retries":
			prog.retries = int(val)
		elif key == "stopsig":
			prog.stopsig = val
		elif key == "stoptime":
			prog.stoptime = int(val)
		elif key == "exitcodes" and type(val) is list:
			prog.exitcodes = val
		elif key == "stdout":
			prog.stdout = val
		elif key == "stderr":
			prog.stderr = val
		elif key == "redir":
			prog.redir = val
		elif key == "envvars" and type(val) is dict:
			prog.envvars = val
		elif key == "workingdir":
			prog.workingdir = val
		elif key == "umask":
			prog.umask = val
	return prog


def loadPrograms(config):
	""""""
	path = os.path.join(os.path.dirname(__file__), config)
	progs = list()
	prog = None

	if os.path.exists(path):
		f = open(path, "r")
		jobj = json.load(f)
		f.close()
		for obj in jobj:
			progs.append(programFromElement(obj))
		return progs
	return None

def saveProgram(program, config, overwrite):
	""""""
	path = os.path.join(os.path.dirname(__file__), config)
	exists = False
	objdump = None
	sdump = None

	if not os.path.exists(path):
		f = open(path, "w")
		f.close()
		objdump = list()
	elif os.path.getsize(path) == 0:
		objdump = list()
	else:
		exists = True
		f = open(path, "r")
		objdump = json.load(f)
		f.close()
	for key, val in vars(program).iteritems():
		if exists == True:
			# objdump[0][key] = val
			print(objdump[0])
		else:
			objdump.append({key:val})
	sdump = json.dumps(objdump, indent=4, separators=(',' , ': '))
	with open(path, "a") as sJSON:
		sJSON.write("\n" + sdump)

# def saveProgram(program, config, overwrite):
# 	""""""
# 	path = os.path.join(os.path.dirname(__file__), config)
# 	objdump = list()
# 	sdump = None
#
# 	if not os.path.exists(path):
# 		f = open(path, "w")
# 		f.close()
# 	for key, val in vars(program).iteritems():
# 			objdump.append({key:val})
# 	sdump = json.dumps(objdump, indent=4, separators=(',' , ': '))
# 	with open(path, "a") as sJSON:
# 		sJSON.write("\n" + sdump)
