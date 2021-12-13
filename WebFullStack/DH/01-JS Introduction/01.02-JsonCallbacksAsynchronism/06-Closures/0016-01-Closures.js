/*
- Funções dentro de funções
- Funções clousers (filhas) acessão as variaveis da função container

*/

function saudacao(nome) {
    let menssagem = "Olá seja bem vindo";

    function juntarNome(){
        return menssagem + ' ' + nome;
    }
    return juntarNome();
}

console.log(saudacao("kris"));