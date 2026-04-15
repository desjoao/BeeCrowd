<?php

$raio = (float) readline();
$area = number_format($raio**2 * 3.14159, 4);
$area = str_replace(',', '', $area);

echo("A={$area}" . "\n");
?>
