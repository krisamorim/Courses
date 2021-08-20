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
        $n1 = $_GET["n1"];
        $n2 = $_GET["n2"];
        $operator = $_GET["operator"];

        switch ($operator){
        case "sum":
            echo $n1.' + '.$n2.' = '.($n1+$n2);
            break;
        case "subt":
            echo $n1.' - '.$n2.' = '.($n1-$n2);
            break;
        case "divi":
            echo $n1.' divided by '.$n2.' = '.($n1/$n2);
            break;
        case "mult":
            echo $n1.' times '.$n2.' = '.($n1*$n2);
        }
    ?>

    <br><br>
    <a href="javascript:history.go(-1)">Back </a>
</body>
</html>