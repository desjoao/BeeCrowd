<?php

function resto_dois($n){
	$lista = [];
	if ($n == 1){
		$lista[] = 2;
		return $lista;
	}
	if ($n == 2){
		return $lista;
	}
	$i = 0;
	for ($j = 0; $j < $n; $j++){
		if ($j%$n == 2){
			$i = $j;
			break;
		}
	}
	while($i <= 10000){
		$lista[] = $i;
		$i+=$n;
	}
	return $lista;
	}

function imprime_dividendos($lista){
	if (sizeof($lista) == 0)
		return;
	for ($i = 0; $i < sizeof($lista); $i++){
		echo($lista[$i] . "\n");
	}
}

$n = (int) readline();
imprime_dividendos(resto_dois($n));
?>
