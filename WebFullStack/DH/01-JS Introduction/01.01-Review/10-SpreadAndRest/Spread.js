//case 1 (join arrays)
let fruitone = ["banana","pera", "maça"];
let fruitTwo = ["pessego","ameixa","laranja"];

//join arrays
let allFuits = [...fruitone, ...fruitTwo];
//console.log(allFuits);

//case 2 (join objects)
let curso = {
    curso: "Fullstack",
    turno: "Manhã",
    sede: "SaoPaulo"
};

let studentOne= {
    nome: "Denise",
    email: "denise@email.com",
    ...curso //add object cursos within
};

let studentTwo = {
    nome: "Jose",
    email: "jose@email.com",
    ...curso //add curse object within studentTwo
};

//console.log("Student1\n"+studentOne+"\n \nStudent2\n"+studentTwo)

//console.log(studentTwo)

//in fuctions
function letters (...paramts){
    console.log(paramts);
}

letters("a","b","c");