const nomes = ["a", "b", "c", "d"]

//com FOR

//No caso abaixo só mostra até o terceiro elemento

for (let i=0; i<3; i++){
    console.log(nomes[i])
}

console.log(" ") //so uma linha de espaço

//para fazer de acordo com a quantidade de itens do array usamos o length 
for (let i=0; i<nomes.length; i++){
    console.log(nomes[i])
}

console.log(" ") //so uma linha de espaço

//mas a melhor solução é a seguinte
for (nome of nomes){
    console.log(nome)
}