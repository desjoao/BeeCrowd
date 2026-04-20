<?php

$valor = (int) round(readline()*100);

$cemR = $cinquentaR = $vinteR = $dezR = $cincoR = $doisR = $umR = 0;
$cinquentaC = $vintecincoC = $dezC = $cincoC = $umC = 0;

while ($valor - 10000>=0){
	$valor-=10000;
	$cemR +=1;
}
while ($valor - 5000>=0){
	$valor -=5000;
	$cinquentaR +=1;
}
while ($valor - 2000>=0){
	$valor -=2000;
	$vinteR +=1;
}
while ($valor - 1000>=0){
	$valor-=1000;
	$dezR+=1;
}
while ($valor - 500>=0){
	$valor-=500;
	$cincoR+=1;
}
while ($valor - 200 >=0){
	$valor-=200;
	$doisR+=1;
}
if ($valor - 100>=0){
	$valor-=100;
	$umR+=1;
}
if ($valor - 50>=0){
	$valor-=50;
	$cinquentaC+=1;
}
if ($valor - 25>=0){
	$valor-=25;
	$vintecincoC+=1;
}
while ($valor - 10>=0){
	$valor-=10;
	$dezC+=1;
}
if ($valor - 5>=0){
	$valor-=5;
	$cincoC+=1;
}
while ($valor - 1 >= 0){
	$umC+=1;
	$valor-=1;
}
print <<<EOD
NOTAS:
{$cemR} nota(s) de R$ 100.00
{$cinquentaR} nota(s) de R$ 50.00
{$vinteR} nota(s) de R$ 20.00
{$dezR} nota(s) de R$ 10.00
{$cincoR} nota(s) de R$ 5.00
{$doisR} nota(s) de R$ 2.00
MOEDAS:
{$umR} moeda(s) de R$ 1.00
{$cinquentaC} moeda(s) de R$ 0.50
{$vintecincoC} moeda(s) de R$ 0.25
{$dezC} moeda(s) de R$ 0.10
{$cincoC} moeda(s) de R$ 0.05
{$umC} moeda(s) de R$ 0.01\n
EOD;

?>
