<?php

function maiorValor($a, $b){
	return ($a + $b + abs($a - $b)) / 2;
}

$input = readline();
list($a, $b, $c) = explode(" ", $input);

if (maiorValor($a, $b) == $a){
	echo(maiorValor($a, $c) . " eh o maior" . "\n");
}
else{
	echo (maiorValor($b, $c) . " eh o maior" . "\n");
}
?>
