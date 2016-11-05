# Taskmaster

## Python:

<!>
Setting the timer interval in "process_class.py" to 0.1 may give more
	accuracy than 1.0 (every second)

<!>
Problem when a third program is added to config!? Could be my osx vm (memory)
	could also be the writing of stdout and stderr
		|
		V
	seems to be attributed to "restart == always". Need to check
	timer/monitor loops



Problems with reload. Check equality checks in taskmaster.py->reloadConfig(),
	and maybe use 'prog.progname' instead of 'prog' == 'prog2'
		|
		V
	Check starting new programs in reload. Duplicates are created. Could be
		that changed programs are not being removed properly
											^
											|
											It's this!

### TODO:
	- Logging
		- A bit more needed? And Check!
	- Program Aspects:
		- Progname
			- Done!
		- Command
			- Done!
		- Procnum
			- Done!
		- Starttime
			- Done!
		- Restart
			- Done!
		- Retries
			- Done!
		- Autolaunch
			- Done!
		- Stoptime
			- Done!
		- Stopsig
		 	- Done!
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
			- Done!
		- Workingdir
			- Done!
		- Umask
			- Done!

	- TaskMaster Commands:
		- stop
			- Done!
		- start
			- Done!
		- status
			- Done!
		- restart
			- Done!
