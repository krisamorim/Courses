//the callbacks principle in summarize is when a function call another function and back to finish what has to do
//as you can see below there is a function that sel-multimplies, that is, it takes its value and multiplies it by self
function mult(values){
    for(let i=1;i<values.length;i++){
        values[i] *= values[i]
    }
    return values
}

let values = [1,2,3,4,10]
console.log(mult(values))//output [1,4,9,16,100]


//now let's do the same logical, but now a function CALLs other function to catch its logic and come BACK to apply obtained logic
const multipyBy = (n) => n*=n//function that will be call

function multVersion2(valores, funcao){//now function has 2 parameters
    for (let i=0;i<valores.length;i++){
        valores[i] = funcao(valores[i])//now function uses the other function
    }
    return valores
}

let values2 = [1,2,3,4,10]
console.log(multVersion2(values2,multipyBy))