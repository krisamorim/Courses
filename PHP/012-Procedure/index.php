<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Select Number to compute</h1></br>
    <form action="do.php" method="get">
        <select name="n1" id="">
            <?php
            for($x = 1; $x<11;$x++){
                echo  "<option value='$x'>$x</option>";
            }
            ?>
        </select>

        <select name="n2" id="">
            <?php
            for ($y=1;$y<11;$y++){
                echo "<option value='$y'>$y</option>";
            }
            ?>
        </select></br></br>
        <?php
        $operators = ['Addition', 'Subtraction','Multiply','Division'];
      
        for ($x=0;$x<4;$x++){
            echo "<input type='radio' name='operators' value='$operators[$x]'> <label for='$operators[$x]'>$operators[$x]</label></br>";
        }        
        
        ?>
        <input type="submit" value="Compute">
    </form>
</body>
</html>