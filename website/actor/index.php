<?php
include ("../scripts/design.php");

include ("../scripts/intfInfo.php");


$actuators = getActuators();

$html = null;

foreach($actuators as $actuator)
{

  $name = getName($actuator->{'spec'});
  $addr = $actuator->conn->{'addr'};
  $port = $actuator->conn->{'port'};
  $ctrl = null;

  switch ($actuator->{'type'})
  {
    case ACTR_SERVO:
      $ctrl = '
          <tr>
            <input type="hidden" value='. $addr .' name="addr"/>
            <input type="hidden" value='. $port .' name="port"/>
            <td> Grad </td>
            <td> <input class="box-form-input" type="number" value="0" name="value" /> </td>
          </tr>
          <tr>
            <td colspan=2 >
              <input class="box-form-input" type="submit" value="Absenden"/>
            </td>
          </tr>
        ';
    break;

    default:
      /* TO DO - Abfrage von mehreren Werten*/
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
        <div class="box-wrapper">
          <?php echo $html; ?>
        </div>
      </div>
    </div>

  </body>
</html>
