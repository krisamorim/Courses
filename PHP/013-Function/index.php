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
        function sum(){
            $args = func_get_args();
            $tot = func_num_args();
            $v = 0;

            for($x=0;$x<$tot;$x++){
                $v += $args[$x];
            }
            return $v;
        }
        $a = sum(3,2,3);
        echo $a;

    ?>
</body>
</html>