# 题目
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

# 级别 
Medium

# 算法口号
找四边的O点，深度优先标记G, 注意二维数组表示是先高再宽

# 解题思路
Search all edges to find 'O' points, DFS search four directions for each edge O points.
Remark all founded O to G. finally replace G as O and O as X

# 算法归类
<a href="../../../DFS.md">深度优先搜索</a>