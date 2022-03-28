//POP -> remove last item
//PUSH -> add item in the last position
//infdexOf -> get element position
//map -> create new array according specifications

var numbers = [1,2,3,4,5];
console.log('The array is: '+numbers);

//using POP
var lastNumber = numbers.pop()
console.log('item removed is: '+lastNumber);

console.log('Array after POP: '+numbers+'\n')


//using PUSH
numbers.push(7);
console.log("Array after PUSH(7): "+numbers);

//getting the position from element 3
console.log('\nThe element 3 position in the array is:'+numbers.indexOf(3)+'\n')


//using MAP
var arr =['cat', 'dog', 'Appel', 'banaNa']

function transformaParaMaiusculo(palavras){
    return palavras.map(palavra => palavra.toUpperCase())
}

console.log(transformaParaMaiusculo(arr))