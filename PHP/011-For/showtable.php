<?php
    $n1 = $_GET['numbers'];
    echo $numbers;
    for($x=1;$x<11;$x++){
        echo "$n1 x $x = ".($n1*$x)."</br>";
    }
?>
</br>
<a href="javascript:history.go(-1)"> Back </a>