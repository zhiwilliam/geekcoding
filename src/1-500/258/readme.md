# 题目
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

# 级别 
Easy

# 算法口号
This is a fairly straight forward question with a trivia catch

# 解题思路
The real question here is, how do we do this without using loops/recursion and in O(1) time?  
Just by analyzing the information given, this is not something you can deduce through logic in a few minutes.  
The most efficient solution is based on a procedure in modulo arithmatics, called "casting out nines" (https://en.wikipedia.org/wiki/Casting_out_nines).  
I would recommend just remembering that 10^n -1 is always divisible by 9, hence k*10^n % 9 = k for k = 1...8, and 0 for k = 9.  Applying that for each digit, it might get easier to understand how the sum of digits is equal to x % 9 if x is between 1 and 8, and 9 if x = 9.