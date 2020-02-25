# 题目
Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

# 级别 
Medium

# 算法口号
二分法查找，画图找出四种情况。

# 解题思路
这道题是非常经典的二分查找，难点在于它有四种情况需要判定，很难记也不必记。面试时候画图写出条件来。

# 算法归类
<a href="../../../DFS.md">深度优先</a>