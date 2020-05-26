# 题目
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

![image](https://assets.leetcode.com/uploads/2018/10/12/island.png "image")


# 级别 
Easy

# 解题思路
The straight forward way to solve this problem is to iterate through the cells, and keep a tally of the length of the perimeter of each cell for all cells.

However, a much more elgant solution has been posted in the discussion area. I provided a short explanation in the comments.

The solution has space and time complexity of O(m*n) where m and n are the number of rows and columns.

