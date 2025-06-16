using System;

class GCBehaviorDemo
{
    static void Main()
    {
        Console.WriteLine("Initial GC generations: " + GC.MaxGeneration);
        for (int i = 0; i < 10_000; i++)
        {
            var temp = new byte[1024];
        }
        GC.Collect();
        Console.WriteLine("Forced GC completed.");
    }
}
