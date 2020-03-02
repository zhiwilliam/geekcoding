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