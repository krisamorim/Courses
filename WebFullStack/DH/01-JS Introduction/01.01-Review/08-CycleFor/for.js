//count odd
function countOnlyOdd(number){
    var  odd = 0;
    for (i=0; i<number; i++){
        if (i%2!=0) {
            odd++
        }
    }
    return odd;
}

//using if ternary
function countOdd (number){
    let odd=0;
    for (i=0; i<number; i++){
        i%2!=0 ? odd++ : i=i;
    }
    return odd;
}

console.log('The total of odd numbers from 0 to 100 is: '+countOnlyOdd(100));

//papagaio
var texto = "Kris";
function papagaio(texto){
    for (let i=0; i<5; i++){
        console.log(texto);
    }
}

function findNumber5 (numbers){

    for (let i=0;i<numbers.length;i++){
        if(numbers[i]==5){
            console.log("We find the number 5 in the position "+i)
            break
        }else{
            console.log('the element '+i+' is '+numbers[i])
        }
    }
}
console.log(findNumber5([10,20,15,5,6,90]));


/* FOR OF 
let iterable = [10, 20, 30];

for (let value of iterable) {
  console.log(value);
}

Result:
// 10
// 20
// 30
*/