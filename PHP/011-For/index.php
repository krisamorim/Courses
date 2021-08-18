<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Times Table</title>
</head>
<body>
    <form action="showtable.php" method="get">
        <select name="numbers" id="">
            <?php
                for($x=1;$x<11;$x++){
                echo "<option value='$x'>$x</option>";
                }
            ?>
        </select>
        </br></br><input type="submit" value="Show table">
    </form>
</body>
</html>