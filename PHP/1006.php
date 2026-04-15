<?php

$a = (float) readline();
$b = (float) readline();
$c = (float) readline();

$media = ($a*2 + $b*3 + $c*5)/10;
$media = str_replace(',', '', number_format($media, 1));
echo("MEDIA = {$media}" . "\n");

?>

