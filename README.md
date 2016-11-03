# Taskmaster

## Python:

# Problem with programs that run once and quit (What?)

# Exit problems (Tied to below?)

Sometimes, it seems, when trying to stop a process, the kill signal is
	sent at a point during monitoring when the process hasn't started but
	'active' is True. Setting the timer interval in "process_class.py" to
	0.1 may give help as it is more accurate than 1.0 (every second)
	Maybe removing/cleaning Process.pop (Popen) object will help
	 (?)

### TODO:
	- Logging
	- Program Aspects:
		- Progname
			- Done!
		- Command
			- Done!
		- Procnum
			- Done!		(test)
		- Starttime
			- Done!		(?)
		- Restart
			- Done!		(test)
		- Retries
			- Done!		(test)
		- Autolaunch
			- Done!		(test)
		- Stoptime
			-
		- Stopsig
		 	- Done!		(!f)
		- Stderr
			-
		- Stdout
			-
		- Rederr
			-
		- Redout
			-
		- Exitcodes
			- Done!
		- Envvars
			- Done!		(test?)
		- Workingdir
			- Done!		(test?)
		- Umask
			- Done!		(test?)

	- TaskMaster Commands:
		- stop
			- Done!
		- start
			-
		- status
			-
