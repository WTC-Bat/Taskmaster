import threading
import subprocess
import time

class Process(threading.Thread):
	""""""
	def __init__(self, program):
		self.stdout = None
		self.stderr = None
		self.pop = None
		self.program = program
		self.killprocess = False
		threading.Thread.__init__(self)

	def run(self):
		""""""
		args = self.program.command.split()
		self.pop = subprocess.Popen(args, stderr=subprocess.PIPE,
									stdout=subprocess.PIPE, shell=True)
		self.monitor()

	def monitor(self):
		""""""
		self.pop.poll()
		while self.pop.returncode == None:
			time.sleep(1)
			self.monitor()
			# return
		for rcode in self.program.exitcodes:
			if (rcode == self.pop.returncode):
				print "GRACEFUL"
				return
		return ("UNEXPECTED")
