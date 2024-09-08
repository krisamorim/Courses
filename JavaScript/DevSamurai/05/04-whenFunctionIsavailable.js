/*
in this code I'll gonna show you that you can use a function before its declaration only if you create it as a function, it means, if you create it as a variabel you just can use it after declaring it
*/

console.log(selfMutply(10))//output 100

function selfMutply(n){
    return n *= n
}


var selfMultiplyVaraible = function (n) {
    return n*=n
}

console.log(selfMultiplyVaraible(5)) //this code in the line 16 output is 25 but if you move to line 11 (before varaible declaration you'll get an error)