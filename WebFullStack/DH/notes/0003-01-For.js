//creating array
let num = [6,4,8,5,7]

//organizing growing
num.sort();

//show array
console.log(num);

//show one by one case01
for (i=0;i<num.length;i++){
    console.log(`The position ${i} has the value ${num[i]}`);
}

//show one by one case02
for (i in num){
    console.log(`The position ${i} has the value ${num[i]}`);
}