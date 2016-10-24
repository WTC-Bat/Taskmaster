import threading
import subprocess
import time

class Process(threading.Thread):
	""""""
	def __init__(self, progdict):
		threading.Thread.__init__(self)
		self.stdout = None
		self.stderr = None
		self.pop = None
		self.program = progdict
		self.killprocess = False
		self.name = "Thread-" + self.program["progname"]
		self.tim = None

	def run(self):
		""""""
		args = self.program["command"].split()
		self.pop = subprocess.Popen(args, stderr=subprocess.PIPE,
									stdout=subprocess.PIPE, shell=True)
		# self.monitor_timer()
		# self.monitor_loop()

		if (self.killprocess == True):
			self.pop.terminate()

		while self.killprocess == False:
			self.monitor_loop()

	def monitor_timer(self):
		tim = threading.Timer(1.0, self.monitor_timer)
		tim.start()
		self.pop.poll()
		if (self.killprocess == True):
			tim.cancel()
			self.pop.terminate()
			return
		if (self.pop.returncode != None):
			for rcode in self.program["exitcodes"]:
				if (rcode == self.pop.returncode):
					tim.cancel()
					return
			tim.cancel()
			return

	def monitor_loop(self):
		""""""
		self.pop.poll()
		# if (self.killprocess == True):
		# 	self.pop.terminate()
		# 	return
		if (self.pop.returncode != None):
			for rcode in self.program["exitcodes"]:
				if (rcode == self.pop.returncode):
					self.killprocess = True
					return
			self.killprocess = True
			return
		# time.sleep(1)
		# self.monitor_loop()
