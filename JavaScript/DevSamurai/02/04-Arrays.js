
var nomes = ["Jesus","kris", "ana", "samuel","others", {name: "kris", age: 33}];
var umArrayVazio = [];

console.log(nomes[5].age)

console.log("The array length is: "+nomes.length+"\nThe element from position zero is: "+nomes[0]);

console.log("\nA empty array: "+umArrayVazio);

console.log("\nArray nome = "+nomes+"\nAdd God in 1st position the array length change to "+nomes.unshift("God")+"\nThe updated array is = "+nomes);

console.log("\nIf remove "+nomes.pop()+" the new array is: "+ nomes); //remove last element

console.log("\nThe position of the ana element is: "+nomes.indexOf("ana")); //show position