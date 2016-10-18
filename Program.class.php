<?php
require_once("tm_data.php");

class Program
{
	/*Properties*/
	public static $verbose = FALSE;
	public $command = "";				//	path/filename -args
	public $procnum = 1;				//	number of proccesses to start and keep running
	public $autolaunch = TRUE;			//	start the program at launch or not
	public $starttime = 5;				//	the amount of time the program will run for brfore being considered 'started'
	public $restart = "unexpected";		//	when to restart. always|never|unexpected*	(*unexpected exit)
	public $retries = 3;				//	how many times to attempt restarting program before aborting
	public $stopsig = "";				//	signal to be used to stop the program
	public $stoptime = 10;				//	how long to wait after stop before killing the program
	public $exitcodes = array();		//	the program's expected exit code
	public $stdout = "";				//
	public $stderr = "";				//
	public $redir = "";					// ?
	public $envvars = array();			//	environment variables to set before launching program
	public $workingdir = "";			//
	public $umask = "";					// wiki umask

	/*Constructor*/
	function __construct(array $args)
	{
		foreach ($args as $key => $val)
		{
			switch ($key)
			{
				case "cmd":
				case "command":
					//check if valid?
					$this->command = $val;
					break;
				case "procnum":
					if (is_numeric($val) === TRUE)
						if ((int)$val > 0)
							$this->procnum = (int)$val;
					break;
				case "autolaunch":
					if (is_bool($val) === TRUE)
						$this->autolaunch = $val;
					break;
				case "restart":
					if ($val === "always" || $val === "never"
						|| $val === "unexpected")
					{
						$this->restart = $val;
					}
					break;
				case "exitcodes":
					if (is_array($val) === TRUE)
						$this->exitcodes = $val;
					break;
				case "starttime":
					if (is_numeric($val) === TRUE)
						if ((int)$val >= 0)
							$this->starttime = $val;
					break;
				case "retries":
					if (is_numeric($val) === TRUE)
						if ((int)$val >= 0)
							$this->retries = $val;
					break;
				case "stopsig":
					$this->stopsig = $val;
					break;
				case "stoptime":
					if (is_numeric($val) === TRUE)
						if ((int)$val >= 0)
							$this->stoptime = $val;
					break;
				case "stdout":
					$this->stdout = $val;
					break;
				case "stderr":
					$this->stderr = $val;
					break;
				case "redir":
					$this->redir = $val;
					break;
				case "envvars":
					if (is_array($val) === TRUE)
						$this->envvars = $val;
					break;
				case "workingdir":
					$this->workingdir = $val;
					break;
				case "umask":
					if (is_numeric($val) === TRUE)
						$this->umask = $val;
					break;
			}
		}
		if (self::$verbose == TRUE)
			print($this . " constructed" . PHP_EOL);
	}

	/*Destructor*/
	function __destruct()
	{
		if (self::$verbose == TRUE)
			print($this . " destructed" . PHP_EOL);
	}

	/*Functions*/
	public static function doc()
	{
		return (file_get_contents("Program.doc.txt"));
	}

	function __toString()
	{
		$strexitcodes = "";
		$strenvvars = "";
		$strautolaunch = "TRUE";
		$str;

		if (count($this->exitcodes) > 0)
		{
			$cnt = 0;

			foreach ($this->exitcodes as $key => $val)
			{
				if ($cnt > 0)
					$strexitcodes .= "\t\t\t   ";
				$strexitcodes .= $val;
				if ($cnt < (count($this->exitcodes) - 1))
					$strexitcodes .= PHP_EOL;
				// if ($cnt < (count($this->exitcodes) - 1))
				// 	$strexitcodes .= ", ";
				$cnt++;
			}
		}

		if (count($this->envvars) > 0)
		{
			$cnt = 0;

			foreach ($this->envvars as $key => $val)
			{
				if ($cnt > 0)
					$strenvvars .= "\t\t\t   ";
				$strenvvars .= $key . " => " . $val;
				if ($cnt == (count($this->envvars) - 2))
					$strenvvars .= PHP_EOL;
				$cnt++;
			}
		}

		if ($this->autolaunch === FALSE)
			$strautolaunch = "FALSE";

		$str = sprintf
		(
			"Program" . PHP_EOL .
			"{" . PHP_EOL .
			"\tcommand\t\t=> %s" . PHP_EOL .
			"\tprocnum\t\t=> %s" . PHP_EOL .
			"\tautolaunch\t=> %s" .	PHP_EOL .
			"\tstarttime\t=> %d" . PHP_EOL .
			"\trestart\t\t=> %s" . PHP_EOL .
			"\tretries\t\t=> %d" . PHP_EOL .
			"\tstopsig\t\t=> %s" . PHP_EOL .
			"\tstoptime\t=> %d" . PHP_EOL .
			"\texitcodes\t=> %s" . PHP_EOL .
			"\tstdout\t\t=> %s" . PHP_EOL .
			"\tstderr\t\t=> %s" . PHP_EOL .
			"\tredir\t\t=> %s" . PHP_EOL .
			"\tenvvars\t\t=> %s" . PHP_EOL .
			"\tworkingdir\t=> %s" . PHP_EOL .
			"\tumask\t\t=> %s" . PHP_EOL .
			"}",
			$this->command,
			$this->procnum,
			// $this->autolaunch,
			$strautolaunch,
			$this->starttime,
			$this->restart,
			$this->retries,
			$this->stopsig,
			$this->stoptime,
			// $this->exitcodes,
			$strexitcodes,
			$this->stdout,
			$this->stderr,
			$this->redir,
			// $this->envvars,
			$strenvvars,
			$this->workingdir,
			$this->umask
		);
		return ($str);
	}

	function remove($config)
	{
		removeProgram($this, $config);
	}

	function save($config, $overwrite)		//function save($config)
	{
		if ((!file_exists($config)) || (filesize($config) == 0))
			createConfig($config);
		saveProgram($this, $config, $overwrite);
	}

	function p()
	{
		foreach ($this as $key => $val)
		{
			print("$key => $val" . PHP_EOL);
		}
	}
}
?>
