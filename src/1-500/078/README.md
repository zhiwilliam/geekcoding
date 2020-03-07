# 题目
## Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

# 级别 
Medium

# 算法口号
深度优先，只把index后面的传入dfs

# 解题思路
经典的DFS题，每次都先把传入的path加到结果集。再把剩下的值一个一个放入path再递归。

它不存在重复结果的原因是它传递了index。每次for loop都不重新处理index之前的值。那之前的值都是其他递归完成了的。