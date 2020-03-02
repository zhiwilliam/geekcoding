/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {

  public List<List<Integer>> levelOrderBottom(TreeNode root) {
    List<List<Integer>> result = new ArrayList<List<Integer>>();

    levelOrderBottom(root, result, 1);

    return result;
  }

  private void levelOrderBottom(
    TreeNode root,
    List<List<Integer>> result,
    int level
  ) {
    if (root == null) return;

    if (result.size() < level) {
      List<Integer> levelList = new ArrayList<Integer>();
      levelList.add(root.val);
      result.add(0, levelList);
    } else {
      result.get(result.size() - level).add(root.val);
    }

    levelOrderBottom(root.left, result, level + 1);
    levelOrderBottom(root.right, result, level + 1);
  }
}
