/*
#### para fazer de forma manual #### 
1- npm init -y
2- criar arquivo app.js
    2.1 Dentro do arquivo 
    const express = require("express");
    const app = express();
    app.set("view engine", "ejs"); //definindo o motor de views para o ejs
    app.set('view', __dirname + '/pasDasViews'); //para definir a apstas das views
    app.listen(3333, () => {
        console.log("Rodando na porta 3333")
    })


#### para fazer de forma automatica #### 
1- express --view=ejs NomeDaPastaDoProjeto
2- cd entrar na pasta
3- npm install


*/