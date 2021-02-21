        //boolean binary information (true or false)
        var compareBiggerThen = 2 > 1;//show true
        var compareIquality = 2 == 3;//show false
        var compareDifference = 2 != 2;//show false
        var compareHeigherOrEqual = 2 >= 3;//show false
        var comparValueType = 5==="5" //show false, first number and second is string
        //compare Uppercase
        var compareUpperCase = "Z" > "z" //show true

        //print tabble and &&
        console.log("===True Table====\n->AND &&\ntrue&&true: "+(true&&true)+"\ntrue&&false: "+(true&&false)+"\nfalse&&false: "+(false&&false)+"\nfalse&&true: "+(false&&true));

        //print table or ||
        console.log(">OR ||\ntrue||true: "+(true||true)+"\ntrue||false: "+(true||false)+"\nfalse||false: "+(false||false)+"\nfalse||true: "+(false||true));

        /*PS.: && priority over ||

        precedence
        arithmetic operatos first
        relational operators
        ! not
        &&
        ||
        */