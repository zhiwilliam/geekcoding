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
    int length;
    public int widthOfBinaryTree(TreeNode root) {
        length = 0;
        Map<Integer, Integer> map = new HashMap<>();
        dfs(root, 0, 0, map);
        return length;
    }
    
    private void dfs(TreeNode root,int depth,int position, Map<Integer,Integer> map){
        if(root == null)
            return;
        
        map.putIfAbsent(depth, position);
        length = Math.max(length, position - map.get(depth) + 1);
        
        dfs(root.left, depth + 1, position * 2, map);
        dfs(root.right, depth + 1, position * 2 + 1, map);
    }
}