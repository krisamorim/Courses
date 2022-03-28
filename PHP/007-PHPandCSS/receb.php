<!DOCTYPE html>
<html lang="en">
<head>

<?php
    $cor = isset($_GET['cor'])?$_GET['cor']:'#000000';
?>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div.test {
            background-color: <?php echo $cor; ?>;
        }
    </style>
</head>
<body>
    <div class="test">
        .
        .
    </div>
    <br>
    <a href="index.php">Voltar</a>
</body>
</html>