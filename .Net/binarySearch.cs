using System;

public class Program
{
    public static int BinaryRecur(int[] arr, int left, int right, int target)
    {
        if (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target)
                return mid;

            if (arr[mid] > target)
                return BinaryRecur(arr, left, mid - 1, target);
            return BinaryRecur(arr, mid + 1, right, target);
        }
        return -1;
    }

    public static int BinaryIter(int[] arr, int left, int right, int target)
    {
        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target)
                return mid;

            if (arr[mid] > target)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return -1;
    }


    public static void Main()
    {
        Console.WriteLine("Hello World");
        int[] arr = { 1, 5, 6, 8, 9, 12, 14, 16, 17, 19, 35, 36, 68, 89 };
        int target = 16;

        int resultRecur = BinaryRecur(arr, 0, arr.Length, target);
        Console.WriteLine($"Found at: {resultRecur}");

        int resultIter = BinaryIter(arr, 0, arr.Length, target);
        Console.WriteLine($"Found at: {resultIter}");
    }
}