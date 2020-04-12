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
    private int[] levelSum;
    public int deepestLeavesSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        this.levelSum = new int[2];
        dfs(root, 1);
        return levelSum[1];
    }

    private void dfs(TreeNode root, int level) {
        if (root == null) {
            return;
        }
        if (level > levelSum[0]) {
            levelSum[0] = level;
            levelSum[1] = root.val;
        } else if (level == levelSum[0]) {
            levelSum[1] += root.val;
        }
        dfs(root.left, level + 1);
        dfs(root.right, level + 1);
        return;
    }
}