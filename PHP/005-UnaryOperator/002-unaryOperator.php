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

        // condition ? if true : if false
        $numX = $_GET["x"];
        $numY = $_GET["y"];

        $texto = $numX>$numY?'O valor de X é maior':'O valor de Y é maior';

        echo $texto;

        // to test type ?x=5&y=1 after .php in the URL
    ?>
</body>
</html>