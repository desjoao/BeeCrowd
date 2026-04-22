<?php

class MaiorValor{

	private $index = -1;
	private $maiorValor = -1;

	function setter($index, $valor){
		$this->index = $index;
		$this->maiorValor = $valor;
	}

	function getter(){
		return [$this->index, $this->maiorValor];
	}

	function printer(){
		$aux = $this->getter();
		$index = $aux[0];
		$maiorValor = $aux[1];
		echo("{$maiorValor}\n{$index}\n");
	}

	function reader(){
		for ($i = 1; $i < 101; $i++){
			$aux = $this->getter();
			$index = $aux[0];
			$maiorValor = $aux[1];
			$n = (int) readline();
			if ($n > $maiorValor){
				$this->setter($i, $n);
			}
		}
	}
}

$maiorValor = new MaiorValor();
$maiorValor->reader();
$maiorValor->printer();
?>
