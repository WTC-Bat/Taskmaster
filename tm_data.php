<?php
function createConfig($path)
{
	$xDoc;
	$xRoot;

	if (!file_exists($path))
		mkdir($path);
	$xDoc = new DOMDocument("1.0", "UTF-8");
	$xDoc->xmlStandalone = TRUE;
	$xDoc->formatOutput = TRUE;
	$xRoot = $xDoc->createElement("Programs");
	$xDoc->appendChild($xRoot);
	$xDoc->save($path);
}

//?
function loadPrograms($config)
{
	$progs = array();
	$args = array();
	$xDoc;
	$xProgs;

	$xDoc = new DOMDocument();
	$xDoc->load($config);
	$xProgs = $xDoc->getElementsByTagName("Program");
	foreach ($xProgs as $xProg)
	{
		foreach ($xProg->childNodes as $child)
		{
			switch ($child->nodeName)
			{
				case "":
				case "":
				case "":
				case "":
				case "":
				case "":
				case "":
				case "":
				case "":
				case "":
			}
		}
	}
}

function programExists(Program $prog, $config)
{
	$xDoc = new DOMDocument();
	$xDoc->load($config);
	$xProgs = $xDoc->getElementsByTagName("Program");

	foreach ($xProgs as $xProg)
	{
		foreach ($xProg->childNodes as $child)
		{
			if ($child->nodeName === "command")
			{
				if ($child->nodeValue == $prog->command)
				{
					return (TRUE);
				}
			}
		}
	}
	return (FALSE);
}

//?
function removeProgram(Program $prog, $config)
{
	$xDoc = new DOMDocument();
	$xRoot;
	$xProgs;
	$xCmd;
	$equ = TRUE;

	$xDoc->preserveWhiteSpace = FALSE;
	$xDoc->formatOutput = TRUE;
	$xDoc->load($config);
	$xRoot = $xDoc->getElementsByTagName("Programs");
	$xProgs = $xRoot[0]->getElementsByTagName("Program");
	//foreach ($xProgs as $xp)
	foreach ($xProgs as $xProg)
	{
		foreach ($xProg->childNodes as $child)
		{
			switch ($child->nodeName)
			{
				case "command":
					if ($child->nodeValue == $prog->command)
						$equ = TRUE;
					break;
			}
		}



		// $xCmd = $xp->getElementsByTagName("command");
		// print($xCmd[0]->nodeValue . PHP_EOL);
		// if ($xCmd[0]->nodeValue == $prog->command)
		// {
		// 	$xRoot[0]->removeChild($xp);
		// 	break;
		// }
	}
	$xDoc->save($config);
}

function saveNewProgram(Program $prog, DOMDocument $xDoc, DOMElement $xProg)
{
	$xEl;
	$xCh;

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
	}
}

function saveProgram(Program $prog, $config, $overwrite)
{
	$xDoc = new DOMDocument();
	$xRoot;
	$xProg;

	if ((!file_exists($config)) || (filesize($config) == 0))
		createConfig($config);
	$xDoc->preserveWhiteSpace = FALSE;
	$xDoc->formatOutput = TRUE;
	$xDoc->load($config);
	$xRoot = $xDoc->getElementsByTagName("Programs");
	$xProg = $xDoc->createElement("Program");
	$xRoot[0]->appendChild($xProg);
	if (programExists($prog, $config) === TRUE)
	{
		if ($overwrite === TRUE)
		{
			removeProgram($prog, $config);
			saveNewProgram($prog, $xDoc, $xProg);
		}
	}
	else
	{
		saveNewProgram($prog, $xDoc, $xProg);
	}
	$xDoc->save($config);
}
?>
