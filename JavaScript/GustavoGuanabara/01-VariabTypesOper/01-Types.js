//Numbers
var num1 = 100; //this is a variable type number
var calc = (20+4)*3;//the parentheses first

//infinity (subtype number)
var infini = Infinity; //zero to infinity
var minusInfini = -Infinity //zero do -Infinity

//String
var text = "thi is a string"//text in double quotes and single quotes
var text = "first line\nSecond line"//using line break

//Concatenate
var twoWords = "21" + "00";//show 2100
var threeWords = "first " + "and " + "second";//show first and second
var number1 = 10;
var number2 = 5;
console.log(`The muber ${number1} is greater than ${number2}`);

//boolean binary information (true or false)
var compareBiggerThen = 2>1;//show true
var compareIquality = 2=="2";//show true, becaus both have the same value
var compareIdentical = 2==="2"//show false, although both have the same value, they aren't the same type the first is a number and second is string
var compareDifference = 2!=2;//show false
var compareHeigherOrEqual = 2>=3;//show false

//SAMPLE
//average of a student's notas
var firstNote = 10;
var secondNote = 9;
var thirdNote = 8;
var fourthNote = 7;
var averageNotes = (10+9+8+7)/4;
var textAboutAverage = "The student's average is: "+averageNotes;
console.log(textAboutAverage);

/*
PS: Variables can beginning with letter, $ or _
can contain numbers provided that beginning with a letter
can contain signs or symbols
can't contain espace
can't be a reservation word
*/