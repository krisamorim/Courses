//defining the system name as a constant
const SYS_NAME = "***** PETSHOP *****"

//showing system name on the console
console.log(SYS_NAME); 

//creating an array with objects like elements 
let listPets = [{
    name: "Bob",
    age: 5,
    race: "Dog",
    owner: "Kris",
    gender: "Male",
    weight: 3.5,
    vaccinated: true,
    services: ["Bath","Vaccine"]
 },
{
    name: "Bob",
    age: 5,
    race: "Dog",
    owner: "Kris",
    gender: "Male",
    weight: 3.5,
    vaccinated: true,
    services: ["Bath","Vaccine"]
 }];

 //function to register a new pet
 function petRegister(name, age, race, owner, gender, weight, vaccinated, services){
    let pet = {
        name, 
        age, 
        race, 
        owner, 
        gender, 
        weight, 
        vaccinated, 
        services,
    }

    //add new pet to listPets using push
    listPets.push(pet)

    //showing a message on the console
    console.log("The pet: " + name + " was successfully added!");
 }
//using the function to add pet Tico
 petRegister("Tico", 10, "cat", "Maria", "Male", 3, false, ["bath"]);

//function to show pets
function viewPetList() {
    for (let i=0;i<listPets.length;i++){
        console.log("------------------");
        console.log("Pet's name: ", listPets[i].name);
        console.log("Pet's race: ", listPets[i].race);
        console.log("Pet's owner: ", listPets[i].owner);
        console.log("Pet's vaccine: ", listPets[i].vaccinated);

        //check if pet is vaccinated
        //console.log(listPets[i].vaccinated ? "The pet is vaccinated" : "The pet needs vaccine");

        //toVaccine(listPets[i]);
        /*
        if (!listPets[i].vaccinated){
            console.log("The pet needs vaccine!")
        }else{
            console.log("The pet is vaccinated!")
        }
        */
    }
}

//show the pet list
viewPetList();
console.log("-----------------------------------------");

//check if pet is vaccinated
function toVaccine(pet){
    if (pet.vaccinated) {
        console.log("This pet doesn't need vaccine!")
    }else{
        pet.vaccinated = true;
        console.log("Pet successfully vaccinated!")
    }
}

//test toVaccine function
toVaccine(listPets[2]);

//test again
toVaccine(listPets[2]);
