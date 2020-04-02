# 题目
## Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

# 级别 
Medium

# 算法口号
双指针相向而行，保留较高者

# 解题思路
用两个指针分别从数组的头和尾相向而行，保留高的那个，用低的那个往对方移动。每次都要计算容积，最后得到最大值。