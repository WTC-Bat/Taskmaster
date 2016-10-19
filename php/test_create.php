<?php

require_once("Program.class.php");
require_once("tm_data.php");

$args1 = array
(
	"command" => "/C/WAMP/php.exe",
	"procnum" => 1,
	"autolaunch" => TRUE,
	"starttime" => 5,
	"restart" => "never",
	"retries" => 2,
	"stopsig" => "SSIG",
	"stoptime" => 10,
	"exitcodes" => array(0, 2, 4, 5),
	"stdout" => "/C/stdout",
	"stderr" => "/C/stderr",
	"redir" => "/C/redir",
	"envvars" => array("ENV1" => "VAL1", "ENV2" => "VAL2"),
	"workingdir" => "/tmp",
	"umask" => "077"
);
$args2 = array
(
	"command" => "/C/UsbFix/UsbFix.exe",
	"procnum" => 1,
	"autolaunch" => TRUE,
	"starttime" => 5,
	"restart" => "never",
	"retries" => 2,
	"stopsig" => "SSIG",
	"stoptime" => 10,
	"exitcodes" => array(0, 2, 4, 5),
	"stdout" => "/C/stdout",
	"stderr" => "/C/stderr",
	"redir" => "/C/redir",
	"envvars" => array("ENV1" => "VAL1", "ENV2" => "VAL2"),
	"workingdir" => "/tmp",
	"umask" => "077"
);
// $args3 = array
// (
// 	"command" => "/C/Games/Darkmod/TheDarkMod.exe",
// 	"procnum" => 1,
// 	"autolaunch" => TRUE,
// 	"starttime" => 5,
// 	"restart" => "never",
// 	"retries" => 2,
// 	"stopsig" => "SSIG",
// 	"stoptime" => 10,
// 	"exitcodes" => array(0, 2, 4, 5),
// 	"stdout" => "/C/stdout",
// 	"stderr" => "/C/stderr",
// 	"redir" => "/C/redir",
// 	"envvars" => array("ENV1" => "VAL1", "ENV2" => "VAL2"),
// 	"workingdir" => "/tmp",
// 	"umask" => "077"
// );

// print(Program::doc());
// Program::$verbose = TRUE;

$prog1 = new Program($args1);
$prog2 = new Program($args2);
saveProgram($prog1, "./config.xml", FALSE);
saveProgram($prog2, "./config.xml", FALSE);
// $prog3 = new Program($args3);
// saveProgram($prog3, "./config.xml", FALSE);
print("XML entries created!" . PHP_EOL);
exit(0);
?>
