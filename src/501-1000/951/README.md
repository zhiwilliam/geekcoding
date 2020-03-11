951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

 

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
 

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].

--------------------------------

Idea:

Recursive approach is the straightforward solution. First of all, root value needs to be equal. Secondly, Left/right child of one tree need to be flip equivalent to the left/right or right/left child of the other tree.

--------------------------------

Runtime: 0 ms, faster than 100.00% of Java online submissions for Flip Equivalent Binary Trees.
Memory Usage: 37.4 MB, less than 5.55% of Java online submissions for Flip Equivalent Binary Trees.

--------------------------------


 