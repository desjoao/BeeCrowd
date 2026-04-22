<?php

$n = (int) readline();
$c = 0;
$r = 0;
$s = 0;

for ($i = 0; $i<$n; $i++){
	$resp = explode(' ', readline());
	if ($resp[1] == 'C')
		$c += (int) $resp[0];
	else if ($resp[1] == 'R')
		$r += (int) $resp[0];
	else
		$s += (int) $resp[0];
}

$total = $c + $r + $s;
$pc = number_format($c * 100 / $total, 2);
$pr = number_format($r * 100 / $total, 2);
$ps = number_format($s * 100 / $total, 2);
echo <<<EOF
Total: {$total} cobaias
Total de coelhos: {$c}
Total de ratos: {$r}
Total de sapos: {$s}
Percentual de coelhos: {$pc} %
Percentual de ratos: {$pr} %
Percentual de sapos: {$ps} %\n
EOF;

?>
