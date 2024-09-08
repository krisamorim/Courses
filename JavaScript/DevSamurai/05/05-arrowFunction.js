//normal way
function selfMultplay(n){
    return n*=n
}
console.log(selfMultplay(10))

//in the variable
var selfMult = function (n){
    return n*=n
}
console.log(selfMult(5))

//arrow function
let selfMultArrow = (n) =>{
    return n*=n
}
console.log(selfMultArrow(2))

//arrow function summarized
let selfMultArrowSummarized = (n) => n*=n //note: if you use {} is mandatory use the word "return"
console.log(selfMultArrowSummarized(9))