# 题目
## Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

# 级别 
Easy

# 算法口号
每一步级台阶都可以是从上一级或者上两级台阶这两种走法过来的

# 解题思路
头一次看到easy难度的动态规划
解题很简单，就是n=1，n=2这两种情况先处理了。然后走到后面每一个台阶的走法都是走到之前那个台阶的走法数量加上走到前前个台阶的走法数量相加。