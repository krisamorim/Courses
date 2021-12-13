//using srepead in objects
/* and arrays
let curso = {
    curso: "Fullstack",
    turno: "Manha",
    sede: "São Paulo"
};

let estudanteUm = {
    nome: "Denise",
    email: "denise@email.com",
    ...curso //spread
};

let estudanteDois = {
    nome: "Jose",
    email: "jose@email.com",
    ...curso //spread
}

console.log(estudanteDois)
*/

//using rest in function
function letras(...paramns){
    console.log(paramns)
}
letras('a','b','c');