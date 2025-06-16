using System;

class SpanDemo
{
    static void Main()
    {
        Span<int> nums = stackalloc int[] { 1, 2, 3, 4, 5 };
        Span<int> sub = nums.Slice(1, 3);

        foreach (var n in sub)
            Console.WriteLine(n);
    }
}
