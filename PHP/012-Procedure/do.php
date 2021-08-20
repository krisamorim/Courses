<?php
    $n1 = $_GET['n1'];
    $n2 = $_GET['n2'];
    $operator = $_GET['operators'];
    
    function sum ($a,$b){
        echo "$a + $b = ".($a+$b);
    }

    function minus ($a,$b){
        echo "$a - $b = ".($a-$b);
    }

    function division ($a,$b){
        echo "$a divide by $b = ".($a/$b);
    }

    function multiply ($a,$b){
        echo "$a times $b = ".($a*$b);
    }

    switch ($operator){
        case 'Addition':
            sum($n1,$n2);
            break;
        case 'Subtraction':
            minus($n1,$n2);
            break;
        case 'Multiply':
            multiply($n1,$n2);
            break;
        case 'Division':
            division($n1,$n2);
            break;
    }
?>