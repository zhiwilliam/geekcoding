# 题目
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

# 级别 
Easy

# 算法口号
One of push() or pop() has to be O(n)

# 解题思路
This is very similar to Problem #225.  

The main challenge is getting the "oldest" element in a queue, since that's not a function supported by stacks. To simulate the behavior, we can pop the stack until we get the element at the bottom, then put everything back in the same order as before. We employ a second stack to help with this process.

However, if we somehow get a hint that after a pop(), the second (helper) stack actually has the "oldest" element in the queue at the top of the stack, then we can use that fact to make future pops more efficient by keeping the second stack as-is, and only transfer items from stack 1 to stack 2 when stack 2 is empty. I would strongly recommend looking at the solution at https://leetcode.com/problems/implement-queue-using-stacks/solution/ to understand it faster.