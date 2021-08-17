<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="compute.php" method="get">
        <?php
        $i = 1;
        $oper = ['Sum', 'Subtract', 'Divide', 'Multiply'];
        while ($i<=3){
            echo "Number $i: <input type='number' name='n$i' min='0' max='9' value='$i' require /><br/>";
            $i++;
        }
        echo "</br>";
        $incRadio = 0;
        while ($incRadio<4){
            echo "<input type='radio' name='oper' value='$oper[$incRadio]'/> <label for='$oper[$incRadio]'>$oper[$incRadio]</label></br>";
            
            $incRadio++;
        }

        ?>
        </br><input type="submit" value="Compute">
    </form>
</body>
</html>