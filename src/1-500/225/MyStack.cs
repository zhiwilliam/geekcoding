// C# just for the sake of C#
public class MyStack
{
    private readonly Queue<int> q;

    /** Initialize your data structure here. */
    public MyStack()
    {
        q = new Queue<int>();
    }

    /** Push element x onto stack. */
    public void Push(int x)
    {
        q.Enqueue(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    public int Pop()
    {
        var length = q.Count;
        for (var i = 0; i < q.Count - 1; i++)
        {
            q.Enqueue(q.Dequeue());
        }
        return q.Dequeue();
    }

    /** Get the top element. */
    public int Top()
    {
        return q.ToArray()[q.Count - 1];
    }

    /** Returns whether the stack is empty. */
    public bool Empty()
    {
        return q.Count == 0;
    }

}