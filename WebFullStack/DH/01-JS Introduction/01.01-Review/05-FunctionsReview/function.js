//Function declared
//sintaxe
function sumFunction (a,b) {
    return a + b;
}

/*
In the case above:
sumFunction -> the function name;
a and b -> are called function parameters;
return -> is what the function will return
*/

//Function expressed (assigned to a variable)
//sintaxe
let sumVariable = function (a,b) {
    return a + b;
}

/*
How to run a function
//sintaxe:
fucntionName();
*/

//Example:
function dividedBy (a,b) {return a/b};
console.log(dividedBy(10,2));


//Example2:
//check if the number is even
function isEven (numberToCheck) {return numberToCheck%2==0}
console.log('10 is even? -> '+isEven(10));
console.log('15 is even? -> '+isEven(15));
//your code must be upper the "returned", because the "return" is the last thing runned in a function

//function reduce to sum numbers and return total
let numbers = [10,20,30];
function sum (...numbers){ //this dot dot dot means spread
    return numbers.reduce((total, number) => total += number);
}
const result = sum(...numbers);

//function to split to convert a string to an array
let name = "Jhon martin brown";
let nameObject = name.split(" ");
console.log(nameObject);
console.log(nameObject[1]);


//run node function.js on terminal

