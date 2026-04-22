<?php

function tomadas($reguas){
	$reguas = explode(" ", $reguas);
	$tomadas = 0;
	for($i = 0; $i < sizeof($reguas); $i++){
		$tomadas += (int) $reguas[$i] - 1;
	}
	return $tomadas +1;
}

$reguas = readline();
echo(tomadas($reguas) . "\n");
?>
