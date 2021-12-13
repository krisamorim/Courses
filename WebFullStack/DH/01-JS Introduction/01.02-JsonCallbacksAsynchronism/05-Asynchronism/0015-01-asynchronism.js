function alarme1(){
    return "Hora de acordar, são 08:00";
}

function alarme2(){
    return "Está perto da sua hora de acordar, são 07:50";
}
setTimeout(function(){
    console.log(alarme1())
}, 2000);
console.log(alarme2());

/*
Pilha de tarefas(call stack) para determianr a ordem em que as tarefas são executadas

Fila de tarefas -> organiza as chamadas para funções por ordem de chegada e nunca irá colocar uma função sobre a outra

LIFO Last in first out

APIS web -> funcionalidades que os navegadores dão ao JS

Event loop -> Monitora quais as funções são executadas e em que momento, tem a capacidade de saber quando a pilha de tarefas está vazia
*/ 