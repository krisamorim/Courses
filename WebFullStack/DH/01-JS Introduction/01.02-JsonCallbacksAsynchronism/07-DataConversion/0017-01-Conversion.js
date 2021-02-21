let texto = "abc123"
let numero = 1.10;
let floa = '12.6'


console.log(typeof(texto));
console.log(typeof(numero));
console.log(parseInt(texto));
console.log(parseFloat('12'));
console.log(parseFloat('9,57'));
console.log(String(['João', 'Maria']))
console.log(Number('Olá'))
console.log(Number(true))
console.log(String(true))

let sub = 2-3;
let soma;
let chovendo = 'true'
console.log(typeof(sub))
console.log(typeof(soma))
/*
typeof(variable) -> show the veriable type
Number('32') //32
Number('1.5') //1.5
Number('-2.24) //-2.24
Number('100 anos') //100
Number('4.5_G') //NaN
Number('n405') //NaN

parseInt('34-F-45') //34
parseInt('1 Jogo') //1
parseInt('lista21) //NaN
parseInt('*42.3') //NaN

parseFloat('12.6') //12
parseFloat('9,27) //9
parseFloat('    6.7    ') //6.7
parseFloat('11.9e') //11.9
parseFloat('resultado: 79.3%') //NaN
parseFloat('78.48%') //78.74%
paseFloat('*42.3') //NaN

*/