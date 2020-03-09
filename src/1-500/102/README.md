# 102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

      3
     / \
    9  20
       /  \
      15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

# 分析
题目要求将二叉树按层遍历，这是***广度优先***的典型应用。一看到这种要求把同一层的所有节点都翻出来的要求，就应该首先想到BFS。
* 时间复杂度： ***O(n)***
* 空间复杂度： ***O(n)***