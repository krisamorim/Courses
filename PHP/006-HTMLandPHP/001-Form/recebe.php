<?php
    $n1 = $_GET['n1'];
    $n2 = $_GET['n2'];
    $operacao = $_GET['operacao'];

    if ($operacao=='soma'){
        echo $n1.' + '.$n2.' = '.($n1+$n2).'<br><br>';
    }else{
        echo $n1.' - '.$n2.' = '.($n1-$n2).'<br><br>';
    }
?>
<a href="index.php">Voltar</a>