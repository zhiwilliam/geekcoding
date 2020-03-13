/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//BFS, one queue for treeNode, one Queue for width
//or we can make another datastruction only contain TreeNode and its current position(col num)
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        Map<Integer, List<Integer>> map = new HashMap<>();
        int min = 0;
        int max = 0;
        Queue<TreeNode> nodes = new LinkedList<>();
        Queue<Integer> cols = new LinkedList<>();
        nodes.offer(root);
        cols.offer(0);
        while(!nodes.isEmpty()) {
            TreeNode cur = nodes.poll();
            int col = cols.poll();
            min = Math.min(min, col);
            max = Math.max(max, col);
            if (!map.containsKey(col)) {
                map.put(col, new ArrayList<Integer>());
            }
            map.get(col).add(cur.val);
            if (cur.left != null) {
                nodes.offer(cur.left);
                cols.offer(col - 1);
            }
            if (cur.right != null) {
                nodes.offer(cur.right);
                cols.offer(col + 1);
            }
        }
        for (int i = min; i <= max; i++) {
            ans.add(map.get(i));
        }
        return ans;
    }
}