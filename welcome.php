<?php
session_start();  
?>
<!DOCTYPE html>
<html>
<head>
	<title>Images in Bootstrap</title>
	<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
	
<!-- 	This link is for accessing Bootstrap Features
 -->	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

	<style type="text/css">
		.panel-body{
			padding: 0;
		}
	</style>

</head>
<body>
<!-- 	This is the JQuery Dependency
 -->	<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
	<!-- Latest compiled and minified JavaScript -->
	
<!-- 	This is the script for Bootstrap
 -->	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


 		<nav class="navbar navbar-default navbar-fixed-top">
		<div class="container">
			<div class="nav-header">
 				<h3 class="navbar-left navbar-center"> Welcome <?php echo $_SESSION["userName"]?></h3>
 				<h3 class="navbar navbar-right navbar-center"><a href="logout.php">Logout</a></h3>
				</div>
			</div>
		</nav>

 	<div class="container" style="margin-top: 200px">
		<div class="row">

			<div class="col-md-4 col-xs-12 col-lg-6">
				<div class="panel panel-primary">
					<div class="panel-heading text-center">
						<h1 class="panel-title"> <a href="">Student Details</a></h1>
					</div>
					<div class="panel-body">
						<img class="img-responsive" src="studentDetailsImage.jpg" style="width: 100%">
					</div>
				</div>
			</div>

			<div class="col-md-4 col-xs-12 col-lg-6">
				<div class="panel panel-primary">
					<div class="panel-heading text-center">
						<h1 class="panel-title"> <a href="">Attendance</a></h1>
					</div>
					<div class="panel-body">
						<img class="img-responsive" src="studentDetailsImage.jpg" style="width: 100%">
					</div>
				</div>
			</div>

			<div class="col-md-4 col-xs-12 col-lg-6">
				<div class="panel panel-primary">
					<div class="panel-heading text-center">
						<h1 class="panel-title"> <a href="">Assessment</a></h1>
					</div>
					<div class="panel-body">
						<img class="img-responsive" src="studentDetailsImage.jpg" style="width: 100%">
					</div>
				</div>
			</div>

			<div class="col-md-4 col-xs-12 col-lg-6">
				<div class="panel panel-primary">
					<div class="panel-heading text-center">
						<h1 class="panel-title"> <a href="">Star Ratings</a></h1>
					</div>
					<div class="panel-body">
						<img class="img-responsive" src="studentDetailsImage.jpg" style="width: 100%">
					</div>
				</div>
			</div>

		</div>

	</div>
	
</body>
</html>


<!-- <img src="http://www.touchonelife.org/wp-content/uploads/2019/04/tl-logo.jpg" alt="Arctica" title="Arctica"> -->