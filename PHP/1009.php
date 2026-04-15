<?php

$nome = readline();
$salario = (double) readline();
$vendas = (double) readline() * 0.15;

$ganhos = str_replace(',', '', number_format(floor(($salario + $vendas)*100)/100, 2, '.', ''));

echo("TOTAL = {$ganhos}" . "\n");

?>
