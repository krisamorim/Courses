//worked but wasn't accept
/*let dobro = num1 => num*2;
let triplo = num2 => num2*3;
function aplicar (num3,funcao){
    return funcao(num3); 
}



//worked and was accept
function dobro(numA){
    return numA*2
}

function triplo(numB){
    return numB*3
}

function aplicar (num3,funcao){
    return funcao(num3); 
}
console.log(aplicar(10,triplo));


//calculator
function somar (numA,numB){
    return numA+numB;
}

function subtrair (numA,numB){
    return numA-numB;
}

function multiplicar (numA,numB){
    return numA*numB;
}

function dividir (numA,numB){
    return numA/numB;
}

function calculadora (numA,numB,funct){
    return funct(numA,numB);
}

*/
//creating a list to facility tests
let list = ['www.globo.com','www.youtube.com','www.facebook.com','www.yahoo.com','br-playground.digitalhouse.com'];

//function to concatenate
function adicionarHttp(url) {
    return "http://"+url;
}

//doing callback
function processar(list,funct){
    let listafinal = [];
    for (i=0;i<list.length;i++){
        listafinal.push(funct(list[i]));
    }
    return listafinal;
}

console.log(processar(list,adicionarHttp));