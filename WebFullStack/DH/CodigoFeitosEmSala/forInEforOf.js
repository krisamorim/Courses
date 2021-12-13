/*
//for in para objetos
var person = {fname:"John", lname:"Doe", age:25};

var text = "";
var x;
for (x in person) {
  console.log(text += person[x] + " ");
}

let carro = {
    carro: 'jaguar',
    placa: 'XYB2345',
    ano: 2021
}
for (propriedade in carro){
    //console.log(carro[propriedade])
    console.log(`${propriedade} é ${carro[propriedade]}`)
}
*/
//for of somente para array
let pratos = ["fondue", "paozinho"]
for (valor of pratos) {
    console.log(valor);
}