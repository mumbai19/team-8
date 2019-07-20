<?php
	session_start();
	$connection = mysqli_connect("localhost", "root", "","exampledb"); 
	$email = $_POST['email'];
	$passw = $_POST['password'];
	if($connection==true){
		$sql = "SELECT email FROM credentials WHERE email LIKE '$email' and password LIKE '$passw'";
		$result = mysqli_query($connection,$sql);
		$count = mysqli_num_rows($result);
		if ($count==1){
			$_SESSION["userName"] = $email;
			header("Location: Welcome.php");
 		}
		else{
			echo "<script>alert('Login Unsuccessful');</script>";	
		}
	}
	else{
		echo "<script>alert('Connection Failure');</script>";
	}
	mysqli_close($connection);
?>
