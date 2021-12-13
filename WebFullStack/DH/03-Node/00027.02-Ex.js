let moduloNativo = require('http');
let moduloInstalado = require('axios');
let moduloProprio = require('./minhaFuncao')

//ex03
let cachorro = require('./cachorro/cachorro.js ')
console.log("O cachorro se chama "+ cachorro.nome + " e tem " +cachorro.idade + " anos")