<?php
function createConfig($path)
{
	$xDoc;
	$xRoot;

	if (!file_exists($path))
		mkdir($path, 0777, TRUE);
	$xDoc = new DOMDocument("1.0", "UTF-8");
	$xDoc->xmlStandalone = TRUE;
	$xDoc->formatOutput = TRUE;
	$xRoot = $xDoc->createElement("Programs");
	$xDoc->appendChild($xRoot);
	$xDoc->save($path);
}

function loadConfig($config)
{
	$progs = array();
	$xDoc = new DOMDocument();
	$xDoc->load($config);
	$xProgs = $xDoc->getElementsByTagName("Program");
	foreach ($xProgs as $xProg)
	{
		if (count($progs) == 0)
			$progs[0] = programFromElement($xProg);
		else
			array_push($progs, programFromElement($xProg));
	}
	return ($progs);
}

function programExists(Program $prog, $config)
{
	$xDoc = new DOMDocument();
	$xProgs;

	$xDoc->load($config);
	$xProgs = $xDoc->getElementsByTagName("Program");
	foreach ($xProgs as $xProg)
	{
		if (programFromElement($xProg) == $prog)
			return (TRUE);
	}
	return (FALSE);
}

function programFromElement(DOMElement $xProgram)
{
	$prog = new Program(array());

	if ($xProgram->nodeName == "Program")
	{
		foreach ($xProgram->childNodes as $child)
		{
			$nval = $child->nodeValue;
			switch ($child->nodeName)
			{
				case "command":
					$prog->command = $nval;
					break;
				case "procnum":
					$prog->procnum = (int)$nval;
					break;
				case "autolaunch":
					if ($nval === "TRUE")
						$prog->autolaunch = TRUE;
					else
						$prog->autolaunch = FALSE;
					break;
				case "starttime":
					$prog->starttime = (int)$nval;
					break;
				case "restart":
					$prog->restart = $nval;
					break;
				case "retries":
					$prog->retries = (int)$nval;
					break;
				case "stopsig":
					$prog->stopsig = $nval;
					break;
				case "stoptime":
					$prog->stoptime = (int)$nval;
					break;
				case "exitcodes":
					if ($child->hasChildNodes())
					{
						$xCodes = $child->getElementsByTagName("code");
						$codes = array();
						foreach ($xCodes as $xCode)
						{
							if (count($codes) == 0)
								$codes[0] = $xCode->nodeValue;
							else
								array_push($codes, $xCode->nodeValue);
						}
						$prog->exitcodes = $codes;
					}
					break;
				case "stdout":
					$prog->stdout = $nval;
					break;
				case "stderr":
					$prog->stderr = $nval;
					break;
				case "redir":
					$prog->redir = $nval;
					break;
				case "envvars":
					if ($child->hasChildNodes())
					{
						$xEnvs = $child->getElementsByTagName("envvar");
						$vars = array();
						foreach ($xEnvs as $xEnv)
						{
							$var = $xEnv->getElementsByTagName("var");
							$val = $xEnv->getElementsByTagName("val");
							$vars[$var[0]->nodeValue] = $val[0]->nodeValue;
						}
						$prog->envvars = $vars;
					}
					break;
				case "workingdir":
					$prog->workingdir = $nval;
					break;
				case "umask":
					$prog->umask = $nval;
					break;
			}
		}
	}
	return ($prog);
}

function removeProgram(Program $prog, $config)
{
	$xDoc;
	$xProgs;

	if (file_exists($config))
	{
		$xDoc = new DOMDocument();
		$xDoc->preserveWhiteSpace = FALSE;
		$xDoc->formatOutput = TRUE;
		$xDoc->load($config);
		$xProgs = $xDoc->getElementsByTagName("Program");
		foreach ($xProgs as $xProg)
		{
			$p = programFromElement($xProg);
			if ($p == $prog)
			{
				$xProg->parentNode->removeChild($xProg);
				$xDoc->save($config);
				break;
			}
		}
	}
}

function saveNewProgram(Program $prog, DOMDocument $xDoc, $config)
{
	$xRoot;
	$xProg;
	$xEl;
	$xCh;

	$xRoot = $xDoc->getElementsByTagName("Programs");
	$xProg = $xDoc->createElement("Program");
	foreach ($prog as $key => $val)
	{
		if (is_array($val))
		{
			$xEl = $xDoc->createElement($key);
			foreach ($val as $k => $v)
			{
				if ($key === "exitcodes")
				{
					$xCh = $xDoc->createElement("code", $v);
				}
				else if ($key === "envvars")
				{
					$xCh = $xDoc->createElement("envvar");
					$xk = $xDoc->createElement("var", $k);
					$xv = $xDoc->createElement("val", $v);
					$xCh->appendChild($xk);
					$xCh->appendChild($xv);
				}
				$xEl->appendChild($xCh);
			}
		}
		else
		{
			if (is_bool($val))
			{
				if ($val === TRUE)
					$vstr = "TRUE";
				else
					$vstr = "FALSE";
			}
			else
			{
				$vstr = $val;
			}
			$xEl = $xDoc->createElement($key, $vstr);
		}
		$xProg->appendChild($xEl);
		$xRoot[0]->appendChild($xProg);
		$xDoc->save($config);
	}
}

function saveProgram(Program $prog, $config, $overwrite)
{
	$xDoc = new DOMDocument();
	$xRoot;
	$xProg;

	if ((file_exists($config) === FALSE) ||
		(trim(file_get_contents($config)) == FALSE))
	{
		createConfig($config);
	}
	$xDoc->preserveWhiteSpace = FALSE;
	$xDoc->formatOutput = TRUE;
	$xDoc->load($config);
	if (programExists($prog, $config) === TRUE)
	{
		// if ($overwrite === TRUE)
		// {
		// 	removeProgram($prog, $config);
		// 	saveNewProgram($prog, $xDoc, $xProg);
		// }
	}
	else
	{
		saveNewProgram($prog, $xDoc, $config);
	}
}
?>
