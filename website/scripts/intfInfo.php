<?php

  include( "lib/libCom.php" );


  $dirPath    = "/opt/RasPiHome/dev/";

  /**
  * returns all of the found actuators
  */
  function getActuators()
  {
    global $dirPath;

    $actors   = array();
    $json     = null;

    for ($i=0x08; $i < 0x78 ; $i++)
    {
      global $dirPath;

      if (is_dir($dirPath . "0x" . dechex($i)))
      {

        $dirContent = scandir($dirPath . "0x" . dechex($i));

        foreach($dirContent as $file)
        {
          if (strcmp($file, "." ) != 0 && strcmp($file, "..") != 0)
          {
            $jsonFile = fopen($dirPath . "0x" . dechex($i) . "/" . $file, "r" ) or die();
            $json = json_decode(fread($jsonFile, fstat($jsonFile)['size']));

            if ($json->{'spec'} >= 0x70)
            {
              $actors[] = $json;
            }
            fclose($jsonFile);
          }
        }
      }
    }

    return $actors;
  }

  function getSensors()
  {
    global $dirPath;

    $sensors   = array();
    $json     = null;

    for ($i=0x08; $i < 0x78 ; $i++)
    {
      global $dirPath;

      if (is_dir($dirPath . "0x" . dechex($i)))
      {

        $dirContent = scandir($dirPath . "0x" . dechex($i));

        foreach($dirContent as $file)
        {
          if (strcmp($file, "." ) != 0 && strcmp($file, "..") != 0)
          {
            $Jfile = fopen($dirPath . "0x" . dechex($i) . "/" . $file, "r" ) or die();
            $json = json_decode(fread($Jfile, fstat($Jfile)['size']));

            if ($json->{'spec'} < 0x70)
            {
              $sensors[] = $json;
            }
            fclose($jsonFile);
          }
        }
      }
    }
    return $sensors;
  }



 ?>
