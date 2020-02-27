/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null)
            return new ArrayList<>();

        Queue<TreeNode> queue = new ArrayDeque<>();
        List<Integer> list = new ArrayList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {

                TreeNode tem = queue.poll();

                if (i == size - 1)
                    list.add(tem.val);

                if (tem.left != null)
                    queue.offer(tem.left);

                if (tem.right != null)
                    queue.offer(tem.right);
            }
        }

        return list;
    }
}