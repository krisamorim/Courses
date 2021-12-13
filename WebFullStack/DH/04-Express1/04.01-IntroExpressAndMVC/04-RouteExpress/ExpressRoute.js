/*ex1:
const express = require('express');
const app = express();

app.get('/home', (req,res) => res.send("Olá, estamos na página home"))
*/

/*
ex2:
const express = require('express');
const app = express();

let boasVindas = "Bem vindo/a, aqui estamos em seu perfil"

app.get('/perfil', (req,res) => res.send(boasVindas))
*/

/*
ex3:
const express = require('express');
const app = express();

let produto = {
    tipoProduto: null,
    preco: null,
    quantidade: null
}

app.get('/produto/adicionar', (req,res) => res.send(produto))
*/



/*
ex4:
const express = require('express');
const app = express();

let produto = {
  tipoProduto: "living",
  preco: 1245,
  quantidade: 300
}

app.post('/produto/criar', (req,res) => res.send(produto))
/
*/