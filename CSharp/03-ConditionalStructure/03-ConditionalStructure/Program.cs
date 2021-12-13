Console.WriteLine("What's your name?");
string name = Console.ReadLine();
var age = 0;

if (name == "kris")
{
    Console.WriteLine("Hi Kris");
    age = 18;
}
else if (name == "ana")
{
    Console.WriteLine("Hi ana");
    age = 17;
}
else
{
    Console.WriteLine("You are not Kris or Ana :(");
}

//using OR
if (name=="kris" || name=="ana")
{
    //using and
    if (age >= 0 && age < 18)
    {
        Console.WriteLine("You can not pass");
    }
    else
    {
        Console.WriteLine("You can pass. Enjoy it!");
    }
}