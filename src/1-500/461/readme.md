# 题目
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

# 级别 
Easy

# 解题思路
The solution is quite intuitive if we know the XOR operator can do the job, and we end up with counting the number of 1's in the binary representation of a integer.

The solution is O(1) time and O(1) space, since the input is limited to 32-bit integers.