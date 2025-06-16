using System;

class LOHDemo
{
    static void Main()
    {
        var largeArray = new byte[85_000];
        Console.WriteLine("Allocated large array on LOH");
        Console.ReadLine();
    }
}
