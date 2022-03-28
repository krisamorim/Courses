
<?php
    //better to use include_once
    include "functions.php";
    $n1 = $_GET["n1"];
    $n2 = $_GET["n2"];
    $n3 = $_GET["n3"];
    $operator = $_GET["operator"];

    switch ($operator) {
        case 'Sum':
            $result = sum($n1, $n2, $n3);
            echo "$n1 + $n2 + $n3 = $result";
            break;
        
        case 'Minus':
            $result = minus($n1, $n2, $n3);
            $res = $n1-$n2;
            echo "$n1 - $n2 = $res<br>";
            echo "$res - $n3 = ".($res-$n3)."<br>";
            echo "$n1 - $n2 - $n3 = $result";
            break;

        case 'Times':
            $result = times($n1, $n2, $n3);
            echo "$n1 x $n2 x $n3 = $result";
            break;
    }

?>