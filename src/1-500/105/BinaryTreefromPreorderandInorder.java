/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTreeHelper(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, map);
    }

    private TreeNode buildTreeHelper(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd,
            Map<Integer, Integer> map) {
        if (preStart > preEnd || inStart > inEnd)
            return null;

        TreeNode root = new TreeNode(preorder[preStart]);

        if (preStart + 1 <= preEnd) {
            int delta = map.get(preorder[preStart]) - inStart;

            root.left = buildTreeHelper(preorder, preStart + 1, preStart + delta, inorder, inStart, inStart + delta - 1,
                    map);

            root.right = buildTreeHelper(preorder, preStart + delta + 1, preEnd, inorder, inStart + delta + 1, inEnd,
                    map);
        }

        return root;
    }
}