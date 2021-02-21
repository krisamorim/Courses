const sysName = "******* PETSHOP AMOR PET  *******"
console.log(sysName)

let listPet=[];
console.log(listPet)

function registerPet(name, years, breed, ja, services) {
    let pet = {name, years, breed, ja, services};
    listPet.push(pet);
    console.log("The Pet: " + name + " successfully added!");
}

registerPet("Tico", 10, "gato", false, ["shower"]);
registerPet("Meg", 1, "dog", "", ["vaccine"]);

function showPets() {
    for (let i = 0; i < listPet.length; i++) {
        console.log("------------------");
        console.log("Pet's name:", listPet[i].name);
        console.log("Pet's breed:", listPet[i].breed);
        console.log("Pet's owner:", listPet[i].years);
        // console.log(listPet[i].vaccinated?"Is pet vaccinated!":"The pet must be vaccinated!");
        //vaccinate(listPet[i])
        // if(!listPet[i].vaccinated){
        //     console.log("The pet must be vaccinated!")
        // }else {
        //     console.log("O pet já está vaccinated!")
        // }
    }
}

// showPets();
// console.log("-----------------------------------------");

function vaccinate(pet) {
    if (pet.ja) {
        console.log("This animal does not need a vaccine");
    } else {
        pet.ja = true;
        console.log("Pet successfully vaccinated!")
    }
}

console.log(listPet[1])
vaccinate(listPet[1]);
console.log("================================")
console.log(listPet[1])
