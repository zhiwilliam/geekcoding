# 题目
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

# 级别 
Medium

# 算法口号
中序遍历或者压栈

# 解题思路
这道题很简单，就是最基本的中序递归。但题目的最后问道能不能用iter的方式来做？那就是压栈了。
所以我给出了两种解法。

# 算法归类
<a href="../../../DFS.md">深度优先</a>