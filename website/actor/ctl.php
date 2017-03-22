<?php

$command = "/opt/RasPiHome/sbin/actuatorctl ". intval($_POST['addr']) ." ". intval($_POST['port']) ." ". intval($_POST['value']);
shell_exec($command);

header("Location: /actor/");
exit();
?>
