<?php

include("../scripts/lib/libCom.php");

$type = $_POST['type'];
$command = "";
$param = "";

switch ($type)
{
  case ACTR_RGBLED:
    $param .= " ". hexdec($value1[1] . $value1[2]); # R
    $param .= " ". hexdec($value1[3] . $value1[4]); # G
    $param .= " ". hexdec($value1[5] . $value1[6]); # B
  break;

  default:
    $i = 1;
    while (isset($_POST['value' . $i ]))
    {
      $param .= " " . $_POST['value' . $i ];
      $i++;
    }
}

$command = "/opt/RasPiHome/sbin/actuatorctl ". intval($_POST['addr']) ." ". intval($_POST['port']) . $param;

shell_exec($command);

header("Location: /actor/");
exit();
?>
