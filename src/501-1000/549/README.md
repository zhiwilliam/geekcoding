# 549. Binary Tree Longest Consecutive Sequence II

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

```python
Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
```

# Analysis

# Source
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
    //very similar to sequence I, just need to return an arrray
    private int maxLength = 0;
    public int longestConsecutive(TreeNode root) {
        if (root == null) {
            return maxLength;
        }
        dfs(root);
        return maxLength;
    }
    
    private int[] dfs(TreeNode root) {
        if (root == null) {
            return new int[2];
        }
        int inr = 1;
        int dcr = 1;
        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        if (root.left != null) {
            if (root.left.val - 1 == root.val) {
                inr = 1 + left[0];
            }
            if (root.left.val + 1 == root.val) {
                dcr = 1 + left[1];
            }
        }
        if (root.right != null) {
            if (root.right.val - 1 == root.val) {
                inr = Math.max(1 + right[0], inr);
            }
            if (root.right.val + 1 == root.val) {
                dcr = Math.max(1 + right[1], dcr);
            }
        }
        
        maxLength = Math.max(maxLength, inr + dcr - 1);
        return new int[]{inr, dcr};
    }
}
```