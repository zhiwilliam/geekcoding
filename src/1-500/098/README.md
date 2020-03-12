# 题目
## Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

# 级别
Medium

# 解题口号
递归，传父节点值到下一个递归进行最大最小判断。

# 解题思路
这道题我完全被误导了。一开始第一眼的感觉就是中序遍历。结果后来才发现是需要把父结点的值带进子节点的递归中去的（因为要和孙子节点比）

根据BST的定义，左子树的值要在(min,mid)之间，右子树的值在(mid,max)之间，这个mid值并不是中位数而是当前节点的值。

定义一个辅助函数，要给这个辅助函数传入当前要判断的节点，当前要判断的这个节点的取值下限和取值上限。然后使用递归即可，每次要计算下一个节点的时候都要根据这个节点是左孩子还是右孩子对其取值的区间进行更新。
