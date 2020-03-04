# 题目
## Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

# 级别 
Medium

# 算法口号
Backtrack

# 解题思路
这题和46题基本一样，唯一的不同就在于要用set跳过所有已经出现过的数字。注意它的set的写法。

# 算法归类
<a href="../../../Backtrack.md">回溯算法</a>