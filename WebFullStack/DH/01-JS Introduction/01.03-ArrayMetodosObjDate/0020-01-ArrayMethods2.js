/*
//map
let numeros = [2,4,6];
let dobroNumeros = numeros.map(function(umNumero){
    return umNumero*2;
});
console.log(dobroNumeros);


//filter
let idades = [15, 39, 45, 100, 10, 23, 16, 17, 18]
let maiores = idades.filter(function(umaIdade){
    return  umaIdade>= 18;
})
console.log(maiores)


//reduce
let numeros = [10,20,15,5,50];
let resultado = numeros.reduce(function(acumulador,umNumero){
    return acumulador+umNumero;
})
console.log(resultado);
*/

//for each
let paises = ["Argentina", "Brasil", "Colombia"];
paises.forEach(function(umPais,indice){
    console.log('O elemento '+umPais+' está na posição '+indice)
});