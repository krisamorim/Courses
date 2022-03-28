'<?php
    $number = $_GET['numbers'];
    $x = 1;
    
    while ($x < 11){
        echo "$number x $x = ".($number*$x)."</br>";
        $x++;
    }
?>
</br>
<a href="javascript:history.go(-1)"> Back </a>