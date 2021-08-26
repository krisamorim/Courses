<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
    include "functions.php";
    $n1 = $_GET["n1"];
    $n2 = $_GET["n2"];
    $n2 = $_GET["n3"];
    $operator = $_GET["operator"];

    switch ($operator) {
        case 'Sum':
            $result = sum($n1, $n2, $n3);
            echo "$n1 + $n2 + $n3 = $result";
            break;
        
        case 'Minus':
            # code...
            break;

        case 'Times':

            break;
    }

?>
</body>
</html>