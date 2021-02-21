const sysName = "******* PETSHOP AMOR PET  *******"

console.log(sysName)
let listPet = [{
        name: "Bob",
        years: 5,
        breed: "dog",
        owner: "Kris",
        genre: "male",
        wight: 3.5,
        vaccinated: true,
        services: ["shower", "Vacina"]
    },
    {
        name: "Meg",
        years: 2,
        breed: "cat",
        owner: "Lucia",
        genre: "female",
        wight: 1.5,
        vaccinated: true,
        services: ["shower"]
    },
    {
        name: "Ananda",
        years: 3,
        breed: 'turtle',
        owner: 'Fernando',
        widgt: 1.5,
        vaccinated: true,
        services: ["vaccine"]
    }
]

function registerPet(name, years, breed, owner, genre, wight, vaccinated, services) {
    let pet = {
        name,
        years,
        breed,
        owner,
        genre,
        wight,
        vaccinated,
        services,
    }

    listPet.push(pet)
    console.log("The Pet: " + name + " successfully added!");
}

registerPet("Meg", 4, "cat", "Angelina", "male", 3, false, ["shower"])

function showPets() {
    for (let i = 0; i < listPet.length; i++) {
        console.log("------------------");
        console.log("Pet's name:", listPet[i].name);
        console.log("Pet's breed:", listPet[i].breed);
        console.log("Pet's owner:", listPet[i].owner);
        // console.log(listPet[i].vaccinated?"Is pet vaccinated!":"The pet must be vaccinated!");

        vaccinate(listPet[i])


        // if(!listPet[i].vaccinated){

        //     console.log("The pet must be vaccinated!")

        // }else {
        //     console.log("Is pet vaccinated!")
        // }
    }
}

showPets();
console.log("-----------------------------------------");


function vaccinate(pet) {
    if (pet.vaccinated) {
        console.log("This animal does not need a vaccine");
    } else {
        pet.vaccinated = true;
        console.log("Pet successfully vaccinated!")
    }
}

vaccinate(listPet[2]);

vaccinate(listPet[2]);