<?php

$n = (int) readline();
$array = [];

while ($n > 0){
	$array[] = (int) readline();
	$n -=1;
}

for ($i = 0; $i < count($array); $i++){
	$x = $array[$i];
	if ($x > 0){
		if ($x % 2 == 0)
			echo ("EVEN POSITIVE\n");
		else
			echo ("ODD POSITIVE\n");
	}
	else if ($x == 0)
		echo ("NULL\n");
	else{
		if ($x % 2 == 0)
			echo("EVEN NEGATIVE\n");
		else
			echo("ODD NEGATIVE\n");
	}
}
?>
