<?php
include ("../scripts/design.php");

include ("../scripts/intfInfo.php");

include ("../connection.php");

$sensors = getSensors();

$html = null;

foreach($sensors as $sensor)
{
  $name = getName($sensor->{'spec'});
  $addr = $sensor->conn->{'addr'};
  $port = $sensor->conn->{'port'};

  $query = "  SELECT value
              FROM sensor_wert
              WHERE address = '$addr'
              AND port = '$port'
              AND id_key = '0'
              ORDER BY timestamp DESC";

  $value = $DBCONN->query($query)->fetch_assoc()['value'];

  $html .= '
  <div class=box-container>
    <div class=box-header>
      <p class=box-topic>'. $name . '</p>
    </div>
    <div class=box-body>
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
          <td> Wert </td>
          <td>'. $value .'</td>
        </tr>
      </table>
    </div>
  </div>

  ';
}

?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>RasPi-Sensors</title>
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
