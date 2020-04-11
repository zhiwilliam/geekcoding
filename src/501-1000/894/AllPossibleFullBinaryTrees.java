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
    Map<Integer, List<TreeNode>> memo = new HashMap<>();
    public List<TreeNode> allPossibleFBT(int N) {
        if (!memo.containsKey(N)) {
            List<TreeNode> ans = new ArrayList<>();
            if (N == 1) {
                ans.add(new TreeNode(0));
            }else if (N % 2 == 1) {
                for (int numLeft = 1; numLeft <= N - 1; numLeft = numLeft + 2) {
                    for (TreeNode left : allPossibleFBT(numLeft)) {
                        for (TreeNode right : allPossibleFBT(N - 1 - numLeft)) {
                            TreeNode newRoot = new TreeNode(0);
                            newRoot.left = left;
                            newRoot.right = right;
                            ans.add(newRoot);
                        }
                    }
                }
            }
            memo.put(N, ans);
        }
        return memo.get(N);
    }
}