<?php

$num1 = $_POST['num1']; 
$num2 = $_POST['num2']; 
$num3 = $_POST['num3']; 
$dbh = new PDO('mysql:host=localhost;dbname=research', root, 'gators99');
$data = $dbh->prepare('Insert into data (num1,num2,num3) values(?,?,?)');
$out = $data->execute([log($num1),log($num2),log($num3)]);
if($out==false) echo 'oops';
else{
	header("Location: cgi-bin/test.py");
} 
?>
