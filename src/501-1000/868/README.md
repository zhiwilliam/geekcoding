# 题目
## Binary Gap
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:

1 <= N <= 10^9


# 级别 
Easy


# 解题思路
distance between '1' and '1'
let`s check all distances in binary representation
10010001101
1. first distance 1001 (from 0 to 3 index) -> distance 3
2.10001 (from 3 to 7) -> distance 4
3.11 (from 7 to 8) -> distance 1
4.101 (from 8 to 10) -> distance 2


the number of zeros between two "1" add one, then choose the max value.



# 算法归类
Math 
