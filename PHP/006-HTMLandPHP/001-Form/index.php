<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <form action="recebe.php" method="get">
            <input type="text" name="n1" placeholder="Type the first number"> <br><br>
            <input type="text" name="n2" placeholder="Type the seconde number"><br><br>
            <select name="operacao"> 
                <option selected disabled>Selecione a operação</option>
                <option value="soma">Soma</option>
                <option value="subtr">Subtração</option>
            </select><br><br>
            <input type="submit" name="calcular" value="calcular">
        </form>
    </div>
</body>
</html>