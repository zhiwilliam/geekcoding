#742. Closest Leaf in a Binary Tree
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

```python
Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

```

Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.

# Analysis
Turn the tree to graph and do BFS on target.
concern case: 1.only one node 2. do not return root

# source code

```java
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
```