//case01
const somar = (numeroA, numeroB) => numeroA + numeroB;
const calculadora = (numeroA , numeroB, operacao) => operacao(numeroA,numeroB);
console.log(calculadora(10,20,somar));

//case02
console.log(calculadora(10,20, (numeroA,numeroB)=>numeroB-numeroA));

//case03
setTimeout(function(){console.log("Hello");}, 1000);

//case04
let meuCallBack = () => console.log('Olá mundo!');
setTimeout( meuCallBack, 1000);

//case05
function nomeCompleto(nome, sobreNome) {
    return nome + ' ' + sobreNome;
};

function saudar(nome, sobreNome, callBack) {
    return 'Olá ' + callBack(nome, sobreNome) + '!';
};
console.log(saudar('João', 'Neves', nomeCompleto));

function iniciais(nome,sobreNome){
    return nome[0] + sobreNome[0];
}
console.log(saudar('João','Neves',iniciais));