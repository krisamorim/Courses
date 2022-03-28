Console.WriteLine("What's your name?");
string name = Console.ReadLine();

if ((name=="kris" || name=="Kris") || (name=="ana" || name=="Ana"))
{
    if (name=="kris" || name=="Kris")
    {
        Console.WriteLine("Hi Kris! You're welcome.");
        Console.WriteLine("How old are you?");
    }
    else
    {
        Console.WriteLine("Hi Ana!. You're welcome");
        Console.WriteLine("How old are you?");
    }
    //using parse
    int agc = int.Parse(Console.ReadLine());

    if (agc < 18)
    {
        Console.WriteLine("Sorry nut you can not pass :(");
    }
    else
    {
        Console.WriteLine("Go ahead and enjoy it");
    }
}
else
{
    Console.WriteLine("Only authorized people");
}