//array
let cores = ['Azulado','Verde','Amarelo','Azul','Preto','Vermelho'];
let [corPreto,corAzul,corVer] = cores

console.log(corPreto);
console.log(corAzul);
console.log(corVer);

//object
let pessoa = {
    nome: 'Kris',
    idade: 35,
    profissionalista: 'Sim',
    profissao: 'Analista de Sistemas',
    series: 'The Big bang theory' 
}

let {nome,profiss} = pessoa;
console.log(nome);
console.log(profiss);

//another way
let arr = ['Roxo','Azul','Amarelo']
let [cor1,cor2,cor3] = arr;
console.log(cor1);
console.log(cor2);
console.log(cor3);