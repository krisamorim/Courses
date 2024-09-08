
//#1st Case: function using a non object variable
function selfMultply(n){ //creating a function just to show that variable's value will not be modified
    return n *= n
}

let justNumber = 10//creating a variable with value 10 to show that its value will not be modified

console.log(selfMultply(justNumber))//printting using variable "justNumber" return will be 100 (10x10)

console.log(justNumber)//when cheking the value of the variable, it reamins 10

//#2nd Case: function USING an object with the same function created previously
const justAnObject = {value: 5} //creating an object
console.log(selfMultply(justAnObject.value))//output: 25
console.log(justAnObject)//output: { value: 5 } 

//3rd Case: New function set an object as input
function selfMutplyWithOIbject(inpu){
    return inpu.value *= inpu.value
}
console.log(selfMutplyWithOIbject(justAnObject)) //output: 25
console.log(justAnObject) //output: { value: 25 }