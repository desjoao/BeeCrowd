<?php

$valor = (int) readline();
echo($valor . "\n");
$cem = 0;
$cinquenta = 0;
$vinte = 0;
$dez = 0;
$cinco = 0;
$dois = 0;
$um = 0;


while ($valor - 100 >= 0){
	$valor-= 100;
	$cem += 1;
}
while ($valor - 50 >= 0){
	$valor -= 50;
	$cinquenta += 1;
}
while ($valor - 20 >= 0){
	$valor -= 20;
	$vinte += 1;
}
while ($valor - 10 >= 0){
	$valor -= 10;
	$dez +=1;
}
while ($valor - 5 >= 0){
	$valor -= 5;
	$cinco +=1;
}
while ($valor - 2 >= 0){
	$valor -= 2;
	$dois += 1;
}
if ($valor >= 0){
	$um = $valor;
	$valor = 0;
}

echo ($cem . " nota(s) de R$ 100,00\n");
echo ($cinquenta . " nota(s) de R$ 50,00\n");
echo ($vinte . " nota(s) de R$ 20,00\n");
echo ($dez . " nota(s) de R$ 10,00\n");
echo ($cinco . " nota(s) de R$ 5,00\n");
echo ($dois . " nota(s) de R$ 2,00\n");
echo ($um . " nota(s) de R$ 1,00\n");
?>
