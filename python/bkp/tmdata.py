import os
import xml.etree.ElementTree as ET
import xml.dom.minidom
from program_class import Program

# def createConfig():
# 	""""""
# 	if not os.path.exists("./config.xml"):
# 		os.makedirs("./config.xml");

def loadConfig(config):
	""""""
	if os.path.exists(config):
		prog = Program()
	else:
		return None

def saveProgram(program, config, overwrite):
	""""""
	programs = None
	program = None
	exitcodes = None
	envvars = None
	var = None
	val = None
	etree = None
	pstr = None

	if not os.path.exists(config):
		cdir = os.path.dirname(__file__)
		cfile = os.path.join(cdir, config)
		f = open(cfile, "w")
		f.close();
	programs = ET.Element("Progams")
	program = ET.SubElement(programs, "Program")
	for key, val in vars(program).iteritems():
		if type(val) is list and key == "exitcodes":
			exitcodes = ET.SubElement(program, "exitcodes")
			for i in val:
				code = ET.SubElement(exitcodes, "code")
				code.text = str(i)
		elif type(val) is dict and key == "envvars":
			envvars = ET.SubElement(program, "envvars")
			for k, v in val:
				envvar = ET.SubElement(envvars, "envvar")
				var = ET.SubElement(envvar, "var")
				val = ET.SubElement(envvar, "val")
				var.text = v
				val.text = k
		else:
			member = ET.SubElement(program, key)
			member.text = val
	etree = ET.ElementTree(programs);
	# pstr = minidom.parseString(ElementTree.tostring(etree, "utf-8"))
	etree.write(os.path.join(os.path.dirname(__file__), config))
