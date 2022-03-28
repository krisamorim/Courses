         //print tabble and &&
         console.log("===True Table====\n->AND &&\ntrue&&true: "+(true&&true)+"\ntrue&&false: "+(true&&false)+"\nfalse&&false: "+(false&&false)+"\nfalse&&true: "+(false&&true));

         //print table or ||
         console.log("->OR ||\ntrue||true: "+(true||true)+"\ntrue||false: "+(true||false)+"\nfalse||false: "+(false||false)+"\nfalse||true: "+(false||true));
 
         function xor(bol1,bol2){
             return (bol1||bol2) && !(bol1&&bol2);
         }
         //print table Xor
         console.log("-> Xor\ntrue xor true: "+xor(true,true)+"\ntrue xor false: "+xor(true,false)+"\nfalse xor true: "+xor(false,true)+"\nfalse xor false: "+xor(false,false));