<?php

$numero = (int) readline();
$horas = (int) readline();
$salarioHora = (float) readline();
$salarioMes = str_replace(',', '', number_format($horas * $salarioHora, 2));

echo("NUMBER = {$numero}" . "\n");
echo("SALARY = U$ {$salarioMes}" . "\n");

?>

