import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
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
	# dom = None
	xdec = "<?xml version='1.0' encoding='utf-8' standalone='yes'?>\n"
	path = None
	f = None
	xdoc = None
	xroot = None
	xel = None

	#	CHECK FOR PROGRAM EXISTENCE

	path = os.path.join(os.path.dirname(__file__), config)
	if not os.path.exists(path):
		f = open(path, "w")
		f.close()
	if os.path.getsize(path) == 0:
		xdoc = MD.Document()
		xroot = xdoc.createElement("Programs")
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
	xdoc.appendChild(xroot)
	# f = open(path, "w")
	# xdoc.writexml(f, indent="\t", addindent="\t", newl="\n")
	# f.close()
	# with open(path, "w") as xml:
		# xml.write(xdoc.toprettyxml(indent="\t", encoding="utf-8"))


"""
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
"""
