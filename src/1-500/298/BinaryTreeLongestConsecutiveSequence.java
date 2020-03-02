class Solution {
    private int maxLength = 0;
    public int longestConsecutive(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root);
        return maxLength;
    }

    private int dfs(TreeNode root) {
        if (root == null) return 0;
        int L = dfs(p.left) + 1;
        int R = dfs(p.right) + 1;
        if (root.left != null && root.val + 1 != root.left.val) {
            L = 1;
        }
        if (root.right != null && root.val + 1 != root.right.val) {
            R = 1;
        }
        int length = Math.max(L, R);
        maxLength = Math.max(maxLength, length);
        return length;
    }
}