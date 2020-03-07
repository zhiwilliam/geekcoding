/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        return checkBalanced(root) == Integer.MIN_VALUE ? false : true;
    }

    private int checkBalanced(TreeNode root) {
        if (root == null)
            return 0;

        int leftHeight = checkBalanced(root.left);
        if (leftHeight == Integer.MIN_VALUE)
            return Integer.MIN_VALUE;

        int rightHeight = checkBalanced(root.right);
        if (rightHeight == Integer.MIN_VALUE)
            return Integer.MIN_VALUE;

        int difference = leftHeight - rightHeight;

        if (Math.abs(difference) > 1) {
            return Integer.MIN_VALUE;
        } else {
            return Math.max(leftHeight, rightHeight) + 1;
        }
    }

}