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
    public int findClosestLeaf(TreeNode root, int k) {
        Map<Integer, Set<Integer>> graph = getGraphFromTree(root);
        if (graph.get(k).size() == 0) {
            return k;
        }
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(k);
        Set<Integer> visited = new HashSet<>();
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            visited.add(cur);
            Set<Integer> nexts = graph.get(cur);
            if (nexts.size() == 1 && cur != root.val) {
                return cur;
            }
            for (int next : nexts) {
                if (!visited.contains(next)) {
                    queue.offer(next);
                }
            }
        }
        return -1;
    }

    private Map<Integer, Set<Integer>> getGraphFromTree(TreeNode root) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        if (root == null) {
            return graph;
        }
        travel(graph, root);
        return graph;
    }

    private void travel(Map<Integer, Set<Integer>> graph, TreeNode root) {
        if (root == null) {
            return;
        }
        Set<Integer> nei = graph.getOrDefault(root.val, new HashSet<Integer>());
        graph.put(root.val, nei);
        nei = graph.get(root.val);
        if (root.left != null) {
            nei.add(root.left.val);
            graph.put(root.val, nei);
            Set<Integer> leftnei = graph.getOrDefault(root.left.val, new HashSet<Integer>());
            leftnei.add(root.val);
            graph.put(root.left.val, leftnei);
        }

        if (root.right != null) {
            nei.add(root.right.val);
            graph.put(root.val, nei);
            Set<Integer> rightnei = graph.getOrDefault(root.right.val, new HashSet<Integer>());
            rightnei.add(root.val);
            graph.put(root.right.val, rightnei);
        }
        travel(graph, root.left);
        travel(graph, root.right);
        return;
    }
}