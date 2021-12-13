//array
let listArray = ['bread','cheese', 'ham', 'tomato', 'carrote', 'lettuce', 'butter'];

console.log(" ========== Variables ========== ");
//show array
console.log("-> Array");
console.log(listArray);

//object
let listObject = {
    name: "Kris",
    genre: "male",
    age: 35,
    children: false
}
//show object
console.log("\n-> Object");
console.log(listObject);
console.log("----------------------------\n");

console.log("============ To JSON ============ ");

//converting array to json
let arrayToJson = JSON.stringify(listArray);
//show the converted array
console.log("-> Array converted:");
console.log(arrayToJson);

//converting object to json
let objectToJson = JSON.stringify(listObject);
//show the converted object
console.log("\n-> Object converted:");
console.log(objectToJson);
console.log("----------------------------\n");

console.log("============= Back ============= ");
//back to array
let jsonToArray = JSON.parse(arrayToJson);
//show 
console.log("Back to array:");
console.log(jsonToArray);

//back to object

let jasonToObject = JSON.parse(objectToJson);
console.log("\nBack to object: ");
console.log(jasonToObject);
console.log("----------------------------\n");