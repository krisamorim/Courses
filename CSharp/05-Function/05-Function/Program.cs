static void checkAge(int age)
{
    if (age < 18)
    {
        Console.WriteLine("Sorry but you can not pass");
    }
    else
    {
        Console.WriteLine("Go ahead and enjoy it");
    }
}

static void checkIdentity (string identity)
{
    if (identity == "Kris" || identity == "Ana")
    {
        if (identity == "Kris")
        {
            Console.WriteLine("\nHi Kris! You're welcome\n");
        }
        else
        {
            Console.WriteLine("Hi Ana! You're welcome");
        }
    }
    else
    {
        Console.WriteLine("You don't have access.");
    }
}
Console.WriteLine("who are you?");
string identity = Console.ReadLine();
checkIdentity(identity);

Console.WriteLine("\nHow old are you?");
int age = int.Parse(Console.ReadLine());
checkAge(age);
