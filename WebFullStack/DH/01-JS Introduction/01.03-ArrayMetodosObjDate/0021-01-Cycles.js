let pessoa = {
    nome: 'Kris',
    idade: 35,
    profissao: 'Desenvolvedor de sistemas'
}

let biblia = ['Jesus','Deus','Maria','José']
//for in
console.log('Os valores são:')
for (let prop in pessoa){
    console.log(prop +': '+pessoa[prop]); //não se pode usar dot notation pessoas.prop
}

//for of
for (let valor of biblia){
    console.log(valor)
}
