var joao = {name: "João", age: 55, gender: "M", AnosContribuicao: '10'}

function verificarSePodeAposentar(age, gender, anosContribuicao){
    if (gender =="F"){
        return age>=60 && anosContribuicao>=30 ? "Pode se aposentar" : "Não Pode se aposentar"; //verdadeiro se mulher tem mais de 60 e contribuiu com pelo menos 30 anos
    } else { //se não for mulher entra aqui
        return age>=65 && anosContribuicao>=30 ? "Pode se aposentar" : "Não Pode se aposentar"; //tem q ser maior de 64 anos e contribuido com pelo menos 30 anos para ser verdadeiro
    }
}

console.log(verificarSePodeAposentar(joao.age, joao.gender, joao.anosContribuicao));