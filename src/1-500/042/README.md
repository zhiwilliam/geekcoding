# 题目
## Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

# 级别 
Hard

# 算法口号
左右向中间扫，低的那个move。逐格计算

# 解题思路
从数组的左右两边往中间扫。如果碰到比自己高就把高度设为新高。碰到比自己低的，就算水有多少（最高高度减去当前高度）。

# 算法归类
<a href="../../../DataStructure.md">数组结构</a>