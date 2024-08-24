//var has the same behavior as a global variable

//1st: create a variable
var x = 10

//2nd: printing at the global scope
console.log("global: ", x)

{
    //3rd: printing at the local scope
    console.log("local: ", x)//as you can see it's worked

    //4th: change value
    x =20
    console.log("After change value: ",x)//as you can see it's worked

    //5th: now creating a var inside a local scope
    var y  = 100
}

//6th: priting var y at the global scope
console.log(y)//as you can see it's worked