# 题目
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

# 级别 
Easy

# 算法口号
Start from both ends, skipping consonants.

# 解题思路
This is an extension of problem 344, with one additional rule (swap vowels only).  

The same idea applies: put a pointer at each end of the array/list, have both traverse toward the middle one place each iteration, while swapping the elements at each pointer.  

However, we have to check if the pointer is at a consonant. If yes, we need to advance that pointer again.  

We also need to check if the first pointer is greater or equal to the one that started at the end. If yes, we should end the loop.  

Time Complexity: O(n) since we need to traverse the array once.
Space Complexity: O(1), we need one additional space to swap the elements.