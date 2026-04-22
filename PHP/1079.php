<?php

class MediaPonderada{
	private $medias;

	function calcula_medias($n){
		for ($i = 0; $i < $n; $i++){
			$entry = explode(' ', readline());
			$valores = array_map('floatval', $entry);
			$this->medias[] = number_format(($valores[0]*2 + $valores[1]*3 + $valores[2]*5) / 10, 1);
		}
	}

	function imprime_medias($n){
		for ($i = 0; $i < $n; $i++){
			echo("{$this->medias[$i]}\n");
		}
	}
}

$n = (int) readline();
$media_ponderada = new MediaPonderada();
$media_ponderada->calcula_medias($n);
$media_ponderada->imprime_medias($n);
?>
