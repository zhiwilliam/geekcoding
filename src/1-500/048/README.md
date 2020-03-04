# 题目
## Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

# 级别 
Medium

# 算法口号
画图，别把i, w, h, width, height 搞错。

# 解题思路
通过画图，搞清楚每个点位需要填入的位置，用一个for 循环把一行上需要移动的点全部都移动。然后利用python的 a,b = b,a的交换性能去设相关值。

# 算法归类
<a href="../../../TE.md">旋转矩阵</a>