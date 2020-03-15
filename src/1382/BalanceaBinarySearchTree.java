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
    //brute force, reconstruct..
    public TreeNode balanceBST(TreeNode root) {
        if (root == null) {
            return null;
        }
        Map<Integer, TreeNode> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        inOrder(root, map, list);
        return buildTree(map, list, 0, list.size() - 1);
    }

    private TreeNode buildTree(Map<Integer, TreeNode> map, List<Integer> list, int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = start + (end - start) / 2;
        TreeNode cur = map.get(list.get(mid));
        cur.left = buildTree(map, list, start, mid - 1);
        cur.right = buildTree(map, list, mid + 1, end);
        return cur;
    }

    private void inOrder(TreeNode root, Map<Integer, TreeNode> map, List<Integer> list){
        if (root == null) {
            return;
        }
        inOrder(root.left, map, list);
        map.put(root.val, root);
        list.add(root.val);
        inOrder(root.right, map, list);
        return;
    }
}