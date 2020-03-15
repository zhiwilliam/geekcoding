/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public TreeNode balanceBST(TreeNode root) {

        List<TreeNode> list = new ArrayList<>();
        storeBST(root, list);
        return buildBST(list, 0, list.size() - 1);
    }

    private void storeBST(TreeNode root, List<TreeNode> list) {
        if (root == null)
            return;

        storeBST(root.left, list);
        list.add(root);
        storeBST(root.right, list);
    }

    private TreeNode buildBST(List<TreeNode> list, int start, int end) {
        if (start > end)
            return null;

        int mid = (start + end) / 2;
        TreeNode node = list.get(mid);

        node.left = buildBST(list, start, mid - 1);
        node.right = buildBST(list, mid + 1, end);

        return node;
    }
}