<?php

$input1 = readline();
list($c1, $q1, $v1) = explode(" ", $input1);
$input2 = readline();
list($c2, $q2, $v2) = explode(" ", $input2);

$total = str_replace(',', '', number_format($q1 * $v1 + $q2 * $v2, 2));
echo ("VALOR A PAGAR: R$ " . $total . "\n");

?>

