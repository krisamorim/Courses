var question = confirm('May I ask you some questions?');
if (question==false){
    alert("Ok! bye bye :)");
}else{
    var nome = prompt("What's your name?");
    while(nome==null || nome==""){
        var nome = prompt("I need to know your name.\nPlease type it:");
    }
alert("Hi "+nome.toUpperCase()+" it's nice to meet you.")
}