var num = [1,-1,2]

function verificaSePositivo(number){
    var verifica = number>0
    switch (verifica){
        case true:
            console.log("positivo")
            break
        case false:
            console.log("negativo")
            break
        default:
            console.log("Não foi possivel verificar")
            break
    }
}

verificaSePositivo(num[1])