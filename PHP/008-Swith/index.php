<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Computer</title>
</head>
<body>
    <form action="comput.php" method="get">
        <input type="text" name="n1" placeholder="Type the first number"><br><br>
        <input type="text" name="n2" placeholder="Type second number"><br><br>
        <input type="radio" name="operator" value="sum" id=""> <label for="sum">Sum</label><br>
        <input type="radio" name="operator" value="subt" id=""> <label for="subt">Subtract</label> <br>
        <input type="radio" name="operator" value="divi" id=""> <label for="divi">Divide</label> <br>
        <input type="radio" name="operator" value="mult" id=""> <label for="mult">Multiply</label> <br>
        
        <br>
        <input type="submit">
    </form>
</body>
</html>