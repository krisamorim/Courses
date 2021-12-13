/*sintax
- the word function is not necessary
- always will be anonymous
- we need attributed them in the a variable
- the sequence of functions comes after the =>
- when we want to return just one sentence the word return and braces are not necessary
- if the arrow receive just one parameter, the parentheses are not necessary

let sum = (num1,num2) => {num1+num2}
sum(2,3); //show 5

let double = num1 => num*2;
double(3); //show 6
*/

const sum = (num1, num2)=>num1+num2;
console.log(sum(3,2));


const somar = (numA, numB) => {
    console.log("Recebi um numero: "+ numA);
    return numA+numB;
}
console.log(somar(20,30));

let currentTime = () => {
    let data = new Date();
    return data.getHours() + ':' + data.getMinutes();
}
console.log(currentTime());