# 题目
## Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

# 题目简介
棋盘字母一笔画（不能是斜线）

# 级别 
Medium

# 算法口号
DFS，注意检查边界，值相等，字符大小写置换和恢复。

# 解题思路
这道题是要把所有board上的字母都进行一次深度递归（一个一个试）。

在深度递归的一开始要检查当下x，y是否在棋盘内，然后字符是否相符。相符的时候要大小写置换防止再次利用。检查完了要记得大小写恢复。
递归是四个方向上都要检查。

这里我发现我有一个很不好的习惯就是喜欢在一个函数里检查四个方向是否都符合条件。应该是检查本格不检查下一步的条件。这个写法贯穿所有的递归题。

