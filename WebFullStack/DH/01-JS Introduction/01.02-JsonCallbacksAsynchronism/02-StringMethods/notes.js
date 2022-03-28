let hi = "Hi, I'm Kris";


//number of characters
console.log("Hi, I'm Kris".length);

//search for the letter i
console.log(hi.indexOf("i"));

//search for the word kris
console.log(hi.indexOf("Kris"));

//take a piece
console.log(hi.slice(0,3));

//delete space at the begining and end of a string
console.log("Without trim:");
console.log("     Hellow    World    \n");
console.log("With trim:");
console.log("     Hellow    World    ".trim());

//convert string in to array
var thisIsString = "God bless you you you you you you you";
console.log(thisIsString.split(' ')); 

//replace the first YOU element found
console.log(thisIsString.replace("you", ""));
console.log(thisIsString.replace(/ /g, '-'));
