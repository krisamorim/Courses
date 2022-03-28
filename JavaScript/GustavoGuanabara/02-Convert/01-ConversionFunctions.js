//Convert number to text
var numberOne = 1;
var addingNumbers = 1 +1; //show 2
var addingNumberAndText = String(numberOne) + 1;//show 11
console.log("var addingNumbers = "+addingNumber+"\nvar addingNumberAndText = "+addingNumberAndText);

//Show type
console.log("The pyte of variable addingNumberAndText is "+typeof(addingNumberAndText));
        
//convert text to number
var numberTwo = "2";
var addingNumbers = Number(numberTwo)+1;//show 3
console.log("var addingNumbers = "+addingNumbers);

//convert to upper case
var textOne = prompt("Please type a text in lower case:");
var convertToUpper = textOne.toUpperCase();
console.log(convertToUpper);
//the same toLowerCase() function