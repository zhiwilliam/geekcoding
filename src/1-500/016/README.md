# 题目
## 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# 级别 
Medium

# 算法口号
排序，三指针暴力求解

# 解题思路
先把数组排序，
然后固定第一个值t，后面两个i，j指针分别指向t的后一个值和最后一个值，相向而行。

如果比target大就把尾端的指针往前移，如果小，就把i往后移。每次都要记录最小误差值。如果无误差立即返回。