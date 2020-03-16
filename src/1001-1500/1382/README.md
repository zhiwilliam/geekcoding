# 1382. Balance a Binary Search Tree
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

```python
Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.

```

#Analysis
Convert the BST to sorted array/list using inorder travel, and then reconstruct the BST to be balance BST

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
```