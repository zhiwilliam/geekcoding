# 题目
## Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
             
# 级别 
Medium

# 算法口号
一行DP。

# 解题思路
找最短路径，有游戏开发经验的同学请不要被它误导成A*算法。因为它只有两个方向可以移动。
所以就是简单地用DP就可以解决。<br>
这道题trick的地方在于它可以反复利用一行空间来进行DP。这种情况其实挺常见，没见过的同学请看代码。