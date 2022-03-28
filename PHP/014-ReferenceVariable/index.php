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
    //function WITHOUT reference
    function test($x){
        $x += 2;
        return $x;
    }
    // creating variable $a
    $a = 2;
    //using $a in test function
    test($a);
    //what value will be shown?
    echo 'Without reference: '.$a.'<br>';
?>


<?php
    //function WITH reference (type & with variable)
    function test2(&$y){
        $y +=2;
        return $y;
    }

    // creating variable $b
    $b = 2;
    test2($b);
    echo 'With reference :'.$b;
?>
</body>
</html>