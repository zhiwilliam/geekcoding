/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
  private int index = 0;

  public TreeNode bstFromPreorder(int[] preorder) {
    return helper(Integer.MIN_VALUE, Integer.MAX_VALUE, preorder);
  }

  private TreeNode helper(int lower, int upper, int[] arr) {
    if (index == arr.length || arr[index] < lower || arr[index] > upper)
      return null;

    int val = arr[index++];
    TreeNode root = new TreeNode(val);
    root.left = helper(lower, val, arr);
    root.right = helper(val, upper, arr);

    return root;
  }
}
