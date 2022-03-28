<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="showtable.php" method="get">
        <select name="numbers" id="">
            <?php
            $x = 1;
            while ($x < 11){
                echo "<option value='$x'>$x</option>";
                $x++;
            }
            ?>
        </select>
        </br></br><input type="submit" value="Show Table">
    </form>
</body>
</html>