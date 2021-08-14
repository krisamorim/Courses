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
        
        echo "<br> <br> Operators:<br> ";
        echo 'pow(3,2)='.(pow(3,2))."<br>";
        echo 'The absolute value of -5 is abs(-5): '.(abs(-5))."<br>";
        echo 'The square root of 56 is sqrt(56): '.(sqrt(56))."<br>";
        echo 'Rounding 3.4 through PHP -> round(3.4): '.(round(3.4)).'<br>';
        echo 'Rounding up 3.4 through PHP -> ceil(3.4): '.(ceil(3.4)).'<br>';
        echo 'Rounding down 3.4 through PHP -> floor(3.4): '.(floor(3.4)).'<br>';
        echo 'Truncating (get the int value) the number 7.7729 through PHP -> intval(7.7729): '.(intval(7.7729)).'<br>';

        
    ?>
</body>
</html>