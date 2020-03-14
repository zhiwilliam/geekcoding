/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    int result = Integer.MIN_VALUE;
    int count = 0;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }

    private void inorder(TreeNode root, int k) {
        if (root == null)
            return;

        inorder(root.left, k);

        count++;

        if (count == k)
            result = root.val;

        inorder(root.right, k);
    }
}