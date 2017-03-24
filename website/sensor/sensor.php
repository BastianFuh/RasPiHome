<?php

$path="/opt/RasPiHome/conf/";
$file="service.conf";

unlink($path.$file);
$file = fopen($path.$file, "w");
echo var_dump($_POST);
fwrite($file, "INTERVAL=". $_POST['interval']);

shell_exec("sudo /bin/systemctl restart RasPiHome.service");

fclose($file);

header("Location: index.php");

exit();
?>
