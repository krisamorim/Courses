<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Compute</h1>
    <form action="compute.php" method="get">
        <?php
            for($x=1;$x<4;$x++){
                echo "<input type='number' name='n$x' placeholder='Type here N$x'><br><br>";
            }
            
            $oper = ['Sum', 'Minus', 'Times'];
            for($x=0;$x<3;$x++){
                echo "$oper[$x]: <input type='radio' name='operator' value='$oper[$x]'></br>";
            }
        ?>
        <br><input type="submit" value="Compute">
    </form>
</body>
</html>