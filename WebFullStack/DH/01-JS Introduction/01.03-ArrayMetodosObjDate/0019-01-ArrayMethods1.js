/*
nome.pop() //remove o ultimo elemnto do array
nome.shift() //remove dados do inicio do array
nome.unshift() // add elementos no inicio do array
*/

let pessoa = ['Vinicius','Kris', true, 'Kris', 23, 3];
console.log(pessoa);

//push
pessoa.push(22); //add 2 a
console.log(pessoa);

//pop
let excluido = pessoa.pop(); //exclui o ultimo elemento e salva na variavelo final do array
console.log(pessoa);
console.log(excluido)

//unshift
pessoa.unshift(24); //add elemento 24 no inicio do array
console.log(pessoa);

//shift
let apagInicio = pessoa.shift() //remove elemento da posição 0 e salva no array
console.log(pessoa)

//indeOf
console.log('a posição do elemento kris (da esquerda para direite) é '+pessoa.indexOf('Kris'))

//includes()
console.log(pessoa.includes('Kris')); //semelahnte ao indexOf mas retorna um boleano true se encontrar

//lastIndexOf
console.log('A posição do elmento Kris (da direita para esquerda é '+pessoa.lastIndexOf('Kris'))

//join
console.log(pessoa.join()) //tranforma array em uma string
console.log(pessoa.join("-")); //transforma em string a array separado com -


var cores = ['Roxo','Laranja', 'Azul'];
cores.push('Violeta');