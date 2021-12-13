//takes contents from a file using native module
/*
const fs = require('fs'); // fs module used to read data from some file

let dados = fs.readFileSync(__dirname + '/stepBystep.txt', 'utf8') //readFileSync takes the contents from a file and __dirname takes the path

console.log(dados)
*/


//using the module that was installed 
let moment = require('moment');

let data = moment().format('MMM do YY')

console.log(data);