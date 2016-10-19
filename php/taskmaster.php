<?php
require_once("Fork.class.php");
require_once("Program.class.php");
require_once("tm_data.php");

function initialize_programs(array $programs)
{
	$pid;
	$out;
	$stat;
	$fork;
	$forks = array();

	foreach ($programs as $program)
	{
		$pid = pcntl_fork();
		if ($pid === -1)
		{
			print("ERROR: could not fork process." . PHP_EOL);
			// exit(1);
		}
		else if ($pid)
		{
			pcntl_wait($status);
		}
		else
		{
			exec($program->command, $out, $stat);
			$fork = new Fork($pid, $program->command, $out, $stat);
			if (count($forks) == 0)
				$forks[0] = $fork;
			else
				array_push($forks, $fork);
			//exit(0);??
		}
	}
	return ($forks);
}

// if (count($argv) > 0)
// {
// 	foreach ($argv as $key => $val)
// 	{
// 		print($val);
// 	}
// }

$config = "./config.xml";
$programs = array();
$done = FALSE;
$stdin;
$in;
$forks;

// if ((file_exists($config) === TRUE) &&
// 	(trim(file_get_contents($config)) !== FALSE))
// {
// 	$programs = loadConfig($config);
// }
$programs = loadConfig($config);
$stdin = fopen("php://stdin", "r");
system("clear");
print("TaskShell> ");
while (!$done)
{
	$in = trim(fgets($stdin));
	if (!empty($in))
	{
		if ($in == "cheese")
			print("Crackers");
		else if ($in == "init")
			if (count($programs) > 0)
				$forks = initialize_programs($programs);
			else
				print("No programs!" . PHP_EOL);
		else if ($in == "forks")
		{
			if (count($forks) > 0)
			{
				foreach ($forks as $key => $val)
				{
					print($key . " => " . $val . PHP_EOL);
				}
				print(PHP_EOL);
			}
			else
			{
				print("No forks!" . PHP_EOL);
			}
		}
		else if ($in == "exit")
			exit(0);
			//$done = TRUE;
		else
			print("Unknown Command");
		if ($done == FALSE)
			print(PHP_EOL . "TaskShell> ");
	}
	// exit(0);
}

?>
