# 题目
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# 级别 
Medium

# 算法口号
旋转数组：
使用方向数组，四边界状态机处理

# 解题思路
这道题初看上去很无厘头，不过仔细看了解法之后，发现还是一道不错的题目。<br>
重点有两个。一个是用方向数组统一了每一步移动的处理方法。另一个是用状态机来处理边界的不断缩小。
最后是用长度来确定什么时候结束循环

# 算法归类
<a href="../../../FSM.md"></a>