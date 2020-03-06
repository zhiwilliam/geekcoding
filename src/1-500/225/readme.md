# 题目
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# 级别 
Easy

# 算法口号
One of push() or pop() has to be O(n)

# 解题思路
There are a few solutions that use methods that are clearly *not allowed*, such as deque.popleft(). According to the question, one can only enqueue, dequeue, and check length.  

2-queue solutions are almost always at a disadvantage, because it can be done with a single queue with the same time complexity.  

If we choose to have O(1) push, which makes more sense to me personally because push() usually gets called more than pop(), then when we pop we can simply cycle the queue until the desired element is in front, then dequeue (O(n)). If we choose to have O(1) pop, then when we push we need to enqueue the new element then cycle the queue until the newest element is in front (O(n)).

# 算法归类
<a href="../../../DataStructure.md">Data Structure</a>
