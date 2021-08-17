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
        $i = 1;
        $oper = $_GET['oper'];

        #creating varied variable
        while ($i<=3){
            #creating n1, n2 and n3
            $n = "n".$i;
            $$n = $_GET["$n"];
            $i++;
        }    
        
        switch ($oper){
            case 'Sum':
                echo $n1.' + '.$n2.' + '.$n3.' = '.($n1+$n2+$n3);
                break;
            case "Subtract":
                echo $n1.' - '.$n2.' - '.$n3.' = '.($n1-$n2-$n3);
                break;
            case "Divide":
                echo $n1.' divided by '.$n2.' divide by '.$n3.' = '.($n1/$n2/$n3);
                break;
            case "Multiply":
                echo $n1.' times '.$n2.' times '.$n3.' = '.($n1*$n2*$n3);

        }


    ?>
</body>
</html>