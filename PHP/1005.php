<?php

$a = (float) readline();
$b = (float) readline();

$media = ($a*3.5+$b*7.5)/11;
$media = str_replace(',', '', number_format($media, 5));
echo ("MEDIA = {$media}" . "\n");

?>

