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

  public TreeNode constructFromPrePost(int[] pre, int[] post) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < post.length; i++) {
      map.put(post[i], i);
    }

    return buildTree(pre, 0, pre.length - 1, post, 0, post.length - 1, map);
  }

  private TreeNode buildTree(
    int[] pre,
    int preS,
    int preE,
    int[] post,
    int postS,
    int postE,
    Map<Integer, Integer> map
  ) {
    if (preS > preE || postS > postE) return null;

    TreeNode root = new TreeNode(pre[preS]);

    if (preS + 1 <= preE) {
      int delta = map.get(pre[preS + 1]) - postS;

      root.left =
        buildTree(
          pre,
          preS + 1,
          preS + 1 + delta,
          post,
          postS,
          postS + delta,
          map
        );
      root.right =
        buildTree(
          pre,
          preS + 1 + delta + 1,
          preE,
          post,
          postS + delta + 1,
          post.length - 1,
          map
        );
    }

    return root;
  }
}
