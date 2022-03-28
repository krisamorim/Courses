<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Retype URL lik: .php?a=10&b=5</h2>
    <?php
        $a = $_GET["a"];
        $b = $_GET["b"];
        echo "$a + $b is ".($a+$b);
    ?>
</body>
</html>