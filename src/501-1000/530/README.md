# 530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
```python
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.
```

# Analysis
Given it's a BST, we can just travel inorder and keep and min difference between adjacent elements.

# Source code

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    //inorder travel and then update distance
    private int ans = Integer.MAX_VALUE;
    private TreeNode prev = null;
    public int getMinimumDifference(TreeNode root) {
        if (root == null) {
            return -1;
        }
        inOrder(root);
        return this.ans;
    }
    
    private void inOrder(TreeNode root) {
        if (root == null) {
            return;
        }
        inOrder(root.left);
        if (this.prev != null) {
            this.ans = Math.min(ans, Math.abs(root.val - this.prev.val));
        }
        this.prev = root;
        inOrder(root.right);
        return;
    }
}
```