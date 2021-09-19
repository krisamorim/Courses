<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <meta http-equiv="refresh" content="3 index.php">
</head>
<body>
    <section id="links">
     <a href="#chr">section chr</a> | <a href="#ord">section ord</a> | <a href="#trim">section trim</a> | <a href="#strlen">section strlen</a> | <a href="#prinf">section printf</a> | <a href="#print_r">section print_r</a> | <a href="#wordwrap">section wordwarp</a> | <a href="#str_word_count">section str_word_count</a> | <a href="#explode">section explode()</a> | <a href="#str_split">Split</a> | <a href="#implode">section implode</a>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="chr">
        <h1>> chr() <</h1>
        To show the ASCI value
        <h3>
        #The code:</br>
        $number = 99;<br>
        print("The ASCI value from $number is ".chr($number));<br>
        <br>
        #The output:<br>
        <?php
        $number = 99;
        print("The ASCI value from $number is ".chr($number));
        ?>
        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="ord">
        <h1>> ord() <</h1>
        Convert value to ASCI
        <h3>
        #The code:</br>
        $value = "X";<br>
        print("The $value in ASCI is ".ord($value));<br>
        <br>
        #The output:<br>
        <?php
        $value = "X";
        print("The $value in ASCI is ".ord($value));
        ?>
        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="strlen">
        <h1> > strlen < </h1>
        <h3>
            #The code:</br>
            $text = "this text has 41 characters (with spaces)"; <br>
            $length = strlen($text);<br>
            echo "The length is $length";<br><br>

            #The final result:</br>
            <?php
                $text = "this text has 41 characters (with spaces)";
                $length = strlen($text);
                echo "The length is $length";
            ?>
        </h3>

        <h4>To check characters' amount</h4>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="trim">
        <h1> > trim < </h1>
        <h3>
            #The code: <br>
            $text = " krishnamurtir ";<br>
            echo "In the word ".$text." there are ".strlen($text).", but after remove spaces from the beginning and the end, there are ". strlen(trim($text)). " characters"; <br><br>

            #The final reult:<br>
            <?php
                $text = " krishnamurtir ";
                echo "In the word ".$text." there are ".strlen($text).", but after remove spaces from the beginning and the end, there are ". strlen(trim($text)). " characters";
            ?>
        </h3>
        <h4>To remove blank from string</h4>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="ltrimAndrtrim">
        <h1>> ltrim And rtrim <</h1>
        <h4>
            ltrim: to remove space from the beginning <br>
            rtrim: to remove the blank space from the end
        </h4>
        <h3>
            #The code: <br>
            $name = " Krishnamurtir " ; <br>
            echo "There are ".strlen($name)." characters in variable &dollar;name "&lt;br&gt;";<br>
            echo "Applying ltrim to remove the spaces from the beginning the variable has only ". strlen(ltrim($name))."&lt;br&gt;";<br>
            echo "After applying rtrim has only ".strlen(rtrim(ltrim($name))); <br><br>

            #Output: <br>
            <?php
            $name = " Krishnamurtir " ;
            echo "There are ".strlen($name)." characters in variable &dollar;name <br>";
            echo "Applying ltrim to remove the spaces from the beginning the variable has only ". strlen(ltrim($name))."<br>";
            echo "After applying rtrim has only ".strlen(rtrim(ltrim($name)));
            ?>
           
        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="printf">
        <!-- Cresting php variables -->
        <h1>> printf <</h1>
        We can write:"The milk costs 3.4", like that:</br>
        <h3>
            <!-- Showing the code and its final result -->
            #The code:<br>
            echo "The $drink costs U$ " . number_format($price,2); </br></br>
            #The final result: <br>
            <?php
            $drink = "milk";
            $price = 0.8; 
            echo "The $drink costs U$".number_format($price,2) 
            ?>
        </h3>

        <h2>or</h2>

        <h3>
            <!-- Showing the code and its final result -->
            #The code:<br>
            printf("The %s costs U$ %.2f", $drink, $price);<br> <!-- %s means it will receive a string value -->
            <br>
            #The final result:<br>
            <?php printf("The %s cost U$ %.2f", $drink, $price)?><br>
            <!--
            %d -> show decimal number (positive or negative)
            %u -> decimal value (without signal, it means, only the positive numbers)
            %f -> to float numbers
            %s -> to string values
            -->
        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="print_r">
        <h1> > Using print_r < </h1>
        <h3>
        #The code: <br>
        $x[0] = 2; <br>
        $x[1] = 4; <br>
        $x[2] = 5; <br> 
        print_r($x); <br> <br>

        #The final result: <br>
        <?php $x[0] = 2; $x[1] = 4; $x[2] = 5; print_r($x);?><br>
        </h3>

        <h4>Is simlar to var_dump($x) and var_export($x);</h4>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="wordwrap">  
        <h1> > wordwrap() <</h1>
        <h3>
        #The code:<br>
        $text = 'here we have long text written to  show how wordwrap worked';<br>
        $withWordWrap = wordwrap($text, 5, "&ltbr/&gt\n", false);<br>
        echo $withWordWrap;
        </h3>

        <h5>
        5: it means each line should have just 5 characters <br>
        &ltbr/&gt\n: &ltbr/&gt to to break line in the page and \n is to break line in the html code </br>
        false: when false doesn't allow to split the word even if it has more than 5 characters <br> 
        </h5>
        
        <h3>#The result:</h3> 
        <?php
        $text = 'Here we have long text written to  show how wordwrap worked';
        $withWordWrap = wordwrap($text, 5, "<br/>\n", false);
        echo $withWordWrap;
        ?>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="str_word_count">
        <h1> > str_word_count < </h1>
        <h4>To count words within strings</h4>
        <h3>
            #The code: <br>
            $text = "Here we have a long text to do the test";<br>
            echo "The number of words in sentence ".$text." is ".str_word_count($text);<br><br>

            #The output: <br>
            <?php
            $text = "Here we have a long text to do the test";
            echo "The number of words in sentence &quot;".$text."&quot; is ".str_word_count($text);
            ?>
            </br>
            <h4> >>Create a array:</h4>
            #The code: <br>
            $textArray = str_word_count($text,1);<br>
            echo "output: ";<br>
            print_r($textArray);<br>
            <br>

            #The output: <br>
            <?php
            $textArray = str_word_count($text,1);
            print_r($textArray);
            ?>

            <h4>>> Create an array with the position of each word</h4>
            #The code: <br>
            $textArray2 = str_word_count($text,2);<br>
            print_r($textArray2);
            <br><br>

            #The output<br>
            <?php
            $textArray2 = str_word_count($text,2);
            print_r($textArray2);
            ?>
        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="explode">
        <h1>> To explode <</h1>
        <h3>
        #The code <br>
        $text = "This is simple text";<br>
        $vector = explode(" ",$text);<br>
        print_r($vector);<br>
        <br>
        #The Output <br>
        <?php 
        $text = "This is simple text";
        $vector = explode(" ",$text);
        print_r($vector);
        ?>

        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="str_split">
        <h1>> split() <</h1>
        <h3>
        #The code:<br>
        $name = "Krishnamurtir";<br>
        $vector = str_split($name);<br>
        print_r($vector);<br>
        <br>
        #The output:<br>
        <?php
        $name = "Krishnamurtir";
        $vector = str_split($name);
        print_r($vector);
        ?>

        </h3>
    </section>
    --------------------------------------------------------------------------------------------------------------------
    <section id="implode">
        <h1>> implode() <</h1>
        <h3>
        #The code:<br>
        $textArray3 = ["My", "name", "is", "Krishnamurtir"];<br>
        $textImplode = implode(" ",$textArray3);<br>
        print($textImplode);<br>
        <br>
        #The output:<br>
        <?php
        $textArray3 = ["My", "name", "is", "Krishnamurtir"];
        $textImplode = implode(" ",$textArray3);
        print($textImplode);
        ?>

        </h3>
    </section>
 </body>
</html>