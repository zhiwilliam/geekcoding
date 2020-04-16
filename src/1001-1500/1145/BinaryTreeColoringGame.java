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
    private int left;
    private int right;
    private int val;
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        this.val = x;
        count(root);
        return Math.max(Math.max(left, right), n - left - right - 1) > n /2; // larger than half then we can win
    }

    private int count(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = count(root.left);
        int r = count(root.right);
        if (root.val == this.val) {
            this.left = l;
            this.right = r;
        }
        return l + r + 1;
    }
}