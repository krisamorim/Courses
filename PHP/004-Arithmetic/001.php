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
        $n1 = 5;
        $n2 = 10;
        $sum = $n1 + $n2;
        echo "1st way: The sum is $sum </br>";
        echo "2nd way: The sum is ".($n1+$n2);
        echo "<br> <br> *Check code to compare";

        echo "<br> <br>";
        echo "n2=$n2 <br>increment is ".++$n2 . "<br>Now n2 is $n2 <br> decrement is ".--$n2;
        

    ?>
</body>
</html>