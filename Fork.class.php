<?php

class Fork
{
	/*Properties*/
	private $_pid;
	private $_command;
	private $_output = array();
	private $_status;

	function __construct($pid, $cmd, $out, $stat)
	{
		$this->_pid = $pid;
		$this->_command = $cmd;
		$this->_output = $out;
		$this->_status = $stat;
	}

	function getPid()
	{
		return ($this->_pid);
	}

	function getCommand()
	{
		return ($this->_command);
	}

	function getOutput()
	{
		return ($this->_output);
	}

	function getStatus()
	{
		return ($this->_status);
	}
}

?>
