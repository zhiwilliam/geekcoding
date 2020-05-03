# 题目
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

# 级别 
Easy

# 解题思路
The core strategy revolves around iterating through both strings simultaneously one character at a time, and adding them after calculating their integer values based on the unicode character (works just like how adding two numbers looks like on paper).

The solution has O(n) time and space complexity.