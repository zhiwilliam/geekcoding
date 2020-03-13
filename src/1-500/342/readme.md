# 题目
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

# 级别 
Easy

# 算法口号
An extension of the "is power of two" problem

# 解题思路
If we know how to check for powers of two, we can build on that knowledge.  

Once integer equal to a power of two is converted into binary, it should be a single 1 followed by all zeroes.  

Alternatively, n (bit-wise AND) (n - 1) should be zero for all powers of two, and non-zero for the complement set, with the exception of n = 0.  

When we have confirmed the integer is a power of two, we simply have to check if the binary representation of the integer has an odd number of bits.
