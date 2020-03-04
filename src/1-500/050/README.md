# 题目
## Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

# 级别 
Medium

# 算法口号
负数次方等于1/x 的正数次方，注意n是奇数偶数的不同。

# 解题思路
这道题有点纯数学的感觉。正数次方很容易，负数次方要复习一下数学定义。

# 算法归类
<a href="../../../TE.md">数学迭代</a>