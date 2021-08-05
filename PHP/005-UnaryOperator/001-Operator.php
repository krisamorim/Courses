<html>
    <?php
    /*
        greater than        >
        less than           <
        greater or equal    >=
        less or equal       <=
        different           <> or !=
        igual               ==
        identical           ===
    */

    $n1 = 7;
    $n2 = 9;
    $result = $n1>$n2?$n1-$n2:$n2-$n1;
    echo '$n1 is '.$n1.' and $n2 is '.$n2.'<br> So $n1 - $n2 = '.($n1-$n2);
    echo "<br> Using unary we have $result <br>";
    echo "-----------------------------------------------------";
    
    $n3 = 7;
    $n4 = "7";
    $resul = $n3==$n4?"Yes":"No";
    $identi = $n3===$n4?"Yes":"No";
    echo '<br> The variable $n3 is '.$n3.' and the variable $n4 is '.$n4.'<br>';
    echo 'Is $n3 equal $n4? --> '.($resul);
    echo '<br>Is $n3 identical $n4? ---> '.($identi);

    ?>
</html>