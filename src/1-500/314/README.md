#314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
```python
Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
```

#Analysis
Using BFS, two queues, one queue for treenode, one queue of level

#Source Code
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
```