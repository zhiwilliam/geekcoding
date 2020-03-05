# 题目
## Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
             
# 级别 
Hard

# 算法口号
DP，不能走的地方标0

# 解题思路
经典的DP题。
检查corner case
然后创建与输入一样的matrix。把第一行和第一列设成1。注意如果输入的第一行（列）里面有阻碍，得把剩余的设成0
然后遍历从第二行第二列开始的所有值。这些值都等于他们的上一行同列和同一行前列的走法之和。
一直算到最后一行最后一列的结果就是总的走法。

一般这种求总的结果不要求具体写出每一个结果值得，基本都可以考虑用DP