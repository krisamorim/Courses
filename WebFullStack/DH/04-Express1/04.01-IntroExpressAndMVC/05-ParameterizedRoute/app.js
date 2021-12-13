const express = require('express');
const app = express();

//creating server
app.listen(3000,() => console.log("Server UP"));


app.get('/', (req,res) => res.send("Olá mundo"))
//=============from here to above is the same code for all =============

/*
series = ["GOT", "Grays An", "The big bang"]
app.get("/series" , (req, res)=> res.send(series))

/*
const express = require('express');
const app = express();

app.get ('/serie/:id', (req, res)=> {
    let idProduto = req.params.id;
    res.send(series[idProduto])
})
*/


//ex01
/*
const express = require('express');
const app = express();

app.get("/series" , (req, res)=>res.send(series))
*/

//ex02
const express = require('express');
const app = express();

app.get ('/serie/:id', (req, res)=> {
    let {id} = req.params;
    res.send(series[id-1])
})