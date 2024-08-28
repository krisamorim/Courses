var person = {
    name: "Julio",
    age: 20,
    city: "Belém"
}

for (let prop in person){
    // console.log(`Prop: ${prop}`)
    console.log(`Prop: ${prop} Value: ${person[prop]}`)
}