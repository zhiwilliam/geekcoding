# 103. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

      3
     / \
    9  20
      /  \
     15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

# 分析
这道题的关键在于在逐层扫描的基础上加上一个方向的控制。用到BFS。
