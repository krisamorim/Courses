let numbers = [10,20,30];
//withou rest
/*let sum = (num1, num2, num3) =>{
    return num1+num2+num3;
}
*/

//with rest using forEach
/*
let sum = (...numbers) => {
    let total = 0;
    numbers.forEach((number) => total += number)
    return total;
}
*/

//with rest using reduce
function sum (...numbers){
    return numbers.reduce((total, number) => total += number);
}
const result = sum(...numbers);
console.log(result);