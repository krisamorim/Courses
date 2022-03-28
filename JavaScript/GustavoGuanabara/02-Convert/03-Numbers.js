var numberOne = 1545.5
console.log(numberOne.toFixed(2)); //add after dot
console.log(numberOne.toFixed(2).replace('.',',')); //replace dot for comma

console.log(numberOne.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})) //Braziliam money in braziliam format


console.log(numberOne.toLocaleString('pt-BR', {style: 'currency', currency: 'USD'})) //American money in braziliam format


console.log(numberOne.toLocaleString('pt-BR', {style: 'currency', currency: 'EUR'})) //Europ money in braziliam format