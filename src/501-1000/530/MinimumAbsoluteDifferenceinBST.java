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
