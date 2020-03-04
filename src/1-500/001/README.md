# 题目
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

# 算法口号
字典存值和序号

# 解题思路
算法题的优化，不是以时间换空间就是以空间换时间。这道题是经典的空间换时间。
算出我满足条件需要的值是哪个？再看这个需要的值是不是在字典里。在的话就找到了，不在的话就把自己的值和序号存入字典。

# 算法归类
<a href="../../../DataStructure.md">字典结构</a>
