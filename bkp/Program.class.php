<?php

/*
**	Constructor accepts only an array of key value pairs. If a property is
**	omitted from the array ('array $args') or the value is incorrect,
**	the default "Property" will be used.
*/
class Program
{
	/*Properties*/
	public $command = "";				//	path/filename -args
	public $procnum = 1;				//	number of proccesses to start and keep running
	public $autolaunch = TRUE;			//	start the program at launch or not
	public $starttime = 5;				//	the amount of time the program will run for brfore being considered 'started'
	public $restart = "unexpected";		//	when to restart. always|never|unexpected*	(*unexpected exit)
	public $retries = 3;				//	how many times to attempt restarting program before aborting
	public $stopsig = "";				//	signal to be used to stop the program
	public $stoptime = 10;				//	how long to wait after stop before killing the program
	public $exitcode = 0;				//	the program's expected exit code
	public $stdout = "";				//
	public $stderr = "";				//
	public $redir = "";					// ?
	public $envvar = array();			//	environment variables to set before launching program
	public $workingdir = "";			//
	public $umask = "";					// wiki umask

	/*Constructor*/
	function __construct(array $args)
	{
		foreach ($args as $arg)
		{
			if (is_array($arg) === TRUE)
			{
				$val = $arg[key($arg)];
				switch (key($arg))
				{
					case "cmd":
					case "command":
						//check if valid?
						$command = $arg[key($arg)];
						break;
					case "procnum":
						if (is_numeric($val) === TRUE)
							if ((int)$val > 0)
								$procnum = $val;
						break;
					case "autolaunch":
						$autolaunch = $arg[key($arg)];
						break;
					case "restart":
						$restart = $arg[key($arg)];
						break;
					case "exitcode":
						$exitcode = $arg[key($arg)];
						break;
					case "starttime":
						$starttime = $arg[key($arg)];
						break;
					case "retries":
						$retries = $arg[key($arg)];
						break;
					case "stopsig":
						$stopsig = $arg[key($arg)];
						break;
					case "stoptime":
						$stoptime = $arg[key($arg)];
						break;
					case "stdout":
						$stdout = $arg[key($arg)];
						break;
					case "stderr":
						$stderr = $arg[key($arg)];
						break;
					case "redir":
						$redir = $arg[key($arg)];
						break;
					case "envvar":
						$envvar = $arg[key($arg)];
						break;
					case "workingdir":
						$workingdir = $arg[key($arg)];
						break;
					case "umask":
						$umask = $arg[key($arg)];
						break;
				}
			}
		}
	}
}

?>
