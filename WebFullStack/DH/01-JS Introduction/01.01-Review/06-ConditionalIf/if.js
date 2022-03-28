//granted access 

var older = 19;
var young = 15;


function checkAccess (yearsOld) {
    if (yearsOld < 13) {
        return 'deny';
    }else if (yearsOld >= 14 && yearsOld <=15) {
        return 'granted, provided that accompanied by those responsible';
    }else {
        return 'granted';
    }
}

console.log('you are older, due this access '+checkAccess(older));
console.log('you are to young, due this access '+ checkAccess(young));