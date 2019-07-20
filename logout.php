<?php 
session_start();
if(isset($_SESSION["userName"])){
	session_unset();
	 if(session_destroy()) {
      header("Location: index.html");
   }
}
?>