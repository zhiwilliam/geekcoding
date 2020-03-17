# 题目
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

# 级别 
Easy

# 算法口号
Start from both ends

# 解题思路
This is a classical interview question that might appear for many entry-level postings.  

The optimal solution is to put a pointer at each end of the array/list, have both traverse toward the middle one place each iteration, while swapping the elements at each pointer.  

Time Complexity: O(n) since we need to traverse the array once.
Space Complexity: O(1), we need one additional space to swap the elements.