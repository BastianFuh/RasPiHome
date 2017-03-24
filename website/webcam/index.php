<?php

include("../scripts/design.php");

?>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="/css/masterstyle.css">
		<title>RasPi-Home</title>
	</head>
	<body>
		<div id="main-wrapper">
			<?php echo $nav; ?>
			<div id="content-wrapper">
        <iframe src="http://192.168.0.2/html" style="border:none;" width="100%" height="100%"></iframe>
			</div>
		</div>
	</body>
</html>
