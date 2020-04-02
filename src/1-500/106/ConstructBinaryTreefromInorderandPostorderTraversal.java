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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || inorder.length == 0 || postorder == null || postorder.length == 0) {
            return null;
        }
        return buildTree(inorder, 0, inorder.length - 1, postorder, postorder.length - 1);
    }

    private TreeNode buildTree(int[] inorder, int instart, int inend, int[] postorder, int postEnd) {
        if (instart > inend) {
            return null;
        }
        TreeNode root = new TreeNode(postorder[postEnd]);
        int val = root.val;
        int index = findIndex(inorder, val);
        int rightTreeLen = inend - index;
        root.right = buildTree(inorder, index + 1, inend, postorder, postEnd - 1);
        root.left = buildTree(inorder, instart, index - 1, postorder, postEnd - rightTreeLen - 1);
        return root;
    }

    private int findIndex(int[] inorder, int val) {
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == val) {
                return i;
            }
        }
        return -1;
    }
}