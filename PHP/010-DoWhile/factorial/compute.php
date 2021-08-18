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

        #$v just to use in the final echo
        $v = $n1;
        echo "<h1>The quantity $n1 is: </h1>";
        $calc = 1;

        do{
            $calc *= $n1;
            $n1--;
        }while ($n1 >= 1);

        echo "<h2>$v! = $calc</h2>";
    ?>

</br>
<a href="javascript:history.go(-1)"> Back </a>
</body>
</html>