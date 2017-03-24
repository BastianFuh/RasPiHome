<?php
include ("../scripts/design.php");

include ("../scripts/intfInfo.php");

error_reporting(E_ALL);

$actuators = getActuators();

$html = null;
$path = "/var/www/html/scripts/lib/dev/";

$actuatorCounter = 0;
foreach($actuators as $actuator)
{
  $actuatorCounter++;
  $spec = $actuator->{'spec'};
  $name = "";
  $addr = $actuator->conn->{'addr'};
  $port = $actuator->conn->{'port'};
  $ctrl = null;

  $filePath = $path . "0x". dechex($spec) . ".json";

  if (file_exists($filePath))
  {
    $file = fopen($filePath, 'r') or die();
    $json = json_decode(fread($file, fstat($file)['size']));

    $name = $json->{'name'};

    $ctrl =  '
        <tr style="height:0px">
          <input type="hidden" value='. $addr .' name="addr"/>
          <input type="hidden" value='. $port .' name="port"/>
          <input type="hidden" value='. $spec .' name="type">
        </tr>';
    $counter = 1;

    foreach($json->attr as $attr)
    {
      $ctrl .='
          <tr>
            <td> '. $attr->{'name'} .' </td>
            <td>
              <input
                  class="box-form-input"
                  type='. $attr->{'type'} .'
                  value="0"
                  name="value'.$counter.'"
                  min='.$attr->{'min'}.'
                  max='.$attr->{'max'}.'
              />
            </td>
          </tr>
          ';
      $counter++;
    }
    $ctrl .= '
        <tr>
          <td colspan=2 >
            <input class="box-form-input" type="submit" value="Absenden"/>
          </td>
        </tr>
      ';
  }

  $html .= '
  <div class=box-container>
    <div class=box-header>
      <p class=box-topic>'. $name . '</p>
    </div>
    <form class="box-body" method="post" action="ctl.php">
      <table class=box-body-content>
          <tr>
            <td> Addresse </td>
            <td> 0x'. dechex($addr) .' </td>
          </tr>
          <tr>
            <td> Port </td>
            <td> 0x'. dechex($port) .' </td>
          </tr>
          <tr>
            <td colspan=2 style="text-align:center"> Steuerung </td>
          </tr>
          '. $ctrl .'
      </table>
    </form method="post" action="profil.php">
    <form class=box-footer >
      <input type="hidden" value='.$addr.' name="addr">
      <input type="hidden" value='.$port.' name="port">
      <input type="submit" value="Profileinstellung" />
    </form>
  </div>

  ';
}

?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>RasPi-Aktoren</title>
    <link rel="stylesheet" href="/css/masterstyle.css">
    <link rel="stylesheet" href="/css/boxLayout.css">
  </head>
  <body>
    <div id="main-wrapper">
      <?php echo $nav; ?>
      <div id="content-wrapper">
        <div class="content-header">
          <h1 class="content-topic"> Aktoren </h1>
          <div class="content-header-info">
            <div class="content-header-box">
              <p class="content-header-box-topic"> Angeschlossene Aktoren </p>
              <p> <?php echo $actuatorCounter ?>  </p> <!--(^-^)-->
            </div>
          </div>
        </div>
        <div class="box-wrapper">
          <?php echo $html; ?>
        </div>
      </div>
    </div>

  </body>
</html>
