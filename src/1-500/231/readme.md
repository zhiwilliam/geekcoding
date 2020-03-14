# 题目
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

# 级别 
Easy

# 算法口号
Use binary representation

# 解题思路
Once the integer is converted into binary, it should be a single 1 followed by all zeroes.
Alternatively, n (bit-wise AND) (n - 1) should be zero for all powers of two, and non-zero for the complement set, with the exception of n = 0.
