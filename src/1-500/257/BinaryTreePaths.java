/*
 * @lc app=leetcode id=257 lang=java
 *
 * [257] Binary Tree Paths
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> list = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        helper(list, root, sb);
        return list;
    }

    private void helper(List<String> list, TreeNode root, StringBuilder sb) {
        if (root == null)
            return;

        int length = sb.length();
        sb.append(root.val);

        if (root.left == null && root.right == null) {
            list.add(sb.toString());
        } else {
            sb.append("->");
            helper(list, root.left, sb);
            helper(list, root.right, sb);
        }
        sb.setLength(length);
    }
}
