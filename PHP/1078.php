<?php

class Tabuada{
	public $tabuada;

	function define_tabuada($n){
		for ($i = 1; $i < 11; $i++){
			$this->tabuada[] = $n * $i;
		}
	}

	function imprime_tabuada($n){
		for ($i = 1; $i < 11; $i++){
			echo ("{$i} x {$n} = {$this->tabuada[$i-1]}\n");
		}
	}
}

$tabuada = new Tabuada();
$n = (int) readline();
$tabuada->define_tabuada($n);
$tabuada->imprime_tabuada($n);
?>
