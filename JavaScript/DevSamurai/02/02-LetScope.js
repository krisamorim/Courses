//let varies depending on scope

//1st: create a variable
let x = 10

//2nd: printing at the global scope
console.log("global: ", x)

{
    //3rd: printing at the local scope
    console.log("local: ", x)//as you can see it's worked

    //4th: change value
    x =20
    console.log("After change value: ",x)//as you can see it's worked

    //5th: now creating a var inside a local scope
    let y  = 100
}

//6th: priting var y at the global scope
console.log(y)//as you can we gat an error