from program_class import Program
import tmdata
import os

def main():
	""""""
	progs = None

	if not os.path.exists("./config.xml"):
		print("\n./config.xml not found!")
		return
	elif os.path.getsize("./config.xml") == 0:
		print("\n./config.xml is empty!")
		return
	progs = tmdata.loadConfig("./config.xml")
	if not progs:
		print("No Progs!")
		return
	for p in progs:
		for k, v in vars(p).iteritems():
			if k == "exitcodes" and type(v) is list:
				print(k)
				for i in v:
					print("\tcode =>" + str(i))
			elif k == "envvars":# and type(v) is dict:
				print(k)
				for dk, dv in v.iteritems():
					print("\t" + dk + " => " + dv)
			else:
				print(k + " => " + str(v))

if __name__ == "__main__":
	main()
