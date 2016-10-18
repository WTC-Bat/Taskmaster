<?php

require_once("Program.class.php");

$args1 = array
(
	"command" => "/C/",
	"procnum" => 1,
	"autolaunch" => FALSE,
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
// print(Program::doc());
// Program::$verbose = TRUE;
$prog1 = new Program($args1);
$prog2 = new Program(array());
$prog3 = new Program(array("Cheese" => "Crackers"));
$prog1->save("./config.xml", TRUE);
$prog2->save("./config.xml", TRUE);
// $prog1->remove("./config.xml");
// print($prog1 . PHP_EOL);
// print($prog2 . PHP_EOL);
// print($prog3 . PHP_EOL);

?>
