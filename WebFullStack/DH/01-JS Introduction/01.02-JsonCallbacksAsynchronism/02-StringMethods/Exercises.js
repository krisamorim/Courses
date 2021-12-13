let addres = "br.digitalhouse.com"
function dominio (addres){
    return "http://"+addres;
}
console.log(dominio(addres));
//------------------------------------

let texto = addres;
console.log(texto.length);
//------------------------------------

function substituicaoRapida(text, wordSearched, wordToReplace){
    return text.replace(wordSearched,wordToReplace);
}
substituicaoRapida("Boa noite","noite","tarde");
//------------------------------------

function menciona (text,word){
    return text.indexOf(word)!==-1 ? true : false;
}
console.log(menciona("Hi my name is kris","ff"));

//------------------------------------
let hicarlos = "Olá, sou Carlos!";
let nomeUsuario = hicarlos.slice(9,15);
console.log(nomeUsuario);

