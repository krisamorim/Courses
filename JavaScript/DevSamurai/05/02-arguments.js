function sum(){
    let total = 0
    for(let n of arguments){
        total+=n
    }
    console.log(total)
}


sum(10,10,10,10,10)