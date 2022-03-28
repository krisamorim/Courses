let courseWeb = {
    course: "Web Full Stack",
    shift: "morning",
    place: "São Paulo"
}

const student ={
    name: 'Lucia',
    age:'30',
    email: 'lucia@email.com',
    ...courseWeb
}

let barra = "===============================================";
console.log(student);
console.log(barra+"/n ")


const car = { model:"HB20", year:2019, type: "gas" }
const owner = { name: "Kris", genre:"male" }
const joinObject = {...car, ...owner};
console.log(joinObject);
console.log(barra)
