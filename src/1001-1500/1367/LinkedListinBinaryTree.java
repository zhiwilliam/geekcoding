/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        List<String> treeList = binaryTreePaths(root);
        String nodeString = nodeListConvert(head);

        for (String str : treeList)
            if (str.contains(nodeString))
                return true;

        return false;
    }

    public String nodeListConvert(ListNode head) {
        ListNode cur = head;
        StringBuilder sb = new StringBuilder();

        while (cur != null) {
            sb.append(Integer.toString(cur.val));
            cur = cur.next;
        }

        return sb.toString();
    }

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> answer = new ArrayList<String>();
        if (root != null)
            searchBT(root, "", answer);
        return answer;
    }

    private void searchBT(TreeNode root, String path, List<String> answer) {
        if (root.left == null && root.right == null)
            answer.add(path + root.val);
        if (root.left != null)
            searchBT(root.left, path + root.val, answer);
        if (root.right != null)
            searchBT(root.right, path + root.val, answer);
    }
}