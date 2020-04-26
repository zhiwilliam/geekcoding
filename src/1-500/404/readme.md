# 题目
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# 级别 
Easy

# 解题思路
The core strategy can revolve around either recursion or iteration.

The recursive strategy is shown in the code, while the iterative strategy can be implemented by keeping a list of nodes to be processed.