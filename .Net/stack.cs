using System;
using System.Collections.Generic;

public class Program
{
    public class MyStack
    {
        public const int MAX_SIZE = 100;
        private int top = -1;
        public int[] stackArray = new int[MAX_SIZE];
        //top = -1;
        //stackArray = new int[MAX_SIZE];

        public void Push(int item)
        {
            if (top >= MAX_SIZE - 1)
            {
                Console.WriteLine("Stack Overflow");
            }
            stackArray[++top] = item;
        }

        public int Pop()
        {
            if (top < 0)
            {
                Console.WriteLine("Stack Undeflow");
            }
            int item = stackArray[top--];
            return item;
        }

        public int Peek()
        {
            if (top < 0)
            {
                Console.WriteLine("Stack Undeflow");
            }
            int item = stackArray[top];
            return item;
        }

        public bool isEmpty()
        {
            return top < 0;
        }

    }

    public static void Main()
    {
        MyStack stack = new MyStack();

        stack.Push(10);
        stack.Push(20);
        stack.Push(30);
        stack.Push(40);
        stack.Push(60);

        Console.WriteLine("Stack Elements:");

        foreach (var item in stack.stackArray)
        {
            Console.WriteLine(item);
        }

        int poped = stack.Pop();
        Console.WriteLine($"\n Popped Element: {poped}");

        int peek = stack.Peek();
        Console.WriteLine($"\n Peeked Element: {peek}");

        bool isEmpty = stack.isEmpty();
        Console.WriteLine($"Is the stack empty? {isEmpty}");
    }
}