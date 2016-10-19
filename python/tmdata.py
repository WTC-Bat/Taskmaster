import os
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
	for k, v in vars(program).iteritems():
		print(k);
	# for m in program:
	# 	print m
