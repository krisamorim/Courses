let person = {
    name: "Ana",
    age: "32",
    address: {street: "Street 7", number: "9", city: "Miami"}
}

console.log(`${person.name} is ${person.age} years old and live in ${person.address.city}`)
console.log(`The ${person.name}'s address is ${person.address}`)//the address does not appear. It's necessary use stringfy as you can see below
console.log(`${JSON.stringify(person.address)}`)