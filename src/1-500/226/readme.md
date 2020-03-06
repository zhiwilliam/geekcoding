# 题目
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

# 级别 
Easy

# 算法口号
Just somehow apply swap(left, right) to all nodes.

# 解题思路
Two ways to do this, both O(n) time and O(n) space:  
1. Recursively apply the function to all nodes starting from the root node
2. Traverse the tree and keep track of unswapped nodes, and swap them
