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
        $n1 = $_GET['n1'];
        $n2 = $_GET['n2'];
        $increment = $_GET['increment'];
        $strtNmbr = 0;

        if ($n2<$n1 || $n1==$n2){
            echo "Last number must be less than first number";
        }else{
            while ($strtNmbr<$n2){
                echo ($n1+$strtNmbr)."</br>";
                $strtNmbr = $strtNmbr + $increment;
            }
        }

    ?>

</br></br>
<a href="javascript:history.go(-1)"> Back </a>
</body>
</html>