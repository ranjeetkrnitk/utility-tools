using System;

public class Program
{
    public static void InsertionSort(int[] arr)
    {
        int n = arr.Length;
        for (int i = 1; i < n; i++)
        {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }


    public static void Main()
    {
        int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
        Console.WriteLine("Original Array:");
        foreach (int num in arr)
        {
            Console.Write(num + " ");
        }

        InsertionSort(arr);

        Console.WriteLine("\nSorted Array:");
        foreach (int num in arr)
        {
            Console.Write(num + " ");
        }
    }
}