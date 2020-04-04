/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class DeleteNodeinaBST {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) return root;
        
        else if(root.val > key)
            root.left = deleteNode(root.left, key);
        else if(root.val < key)
            root.right = deleteNode(root.right, key);
        else{

            //case 1: no child
            if(root.left == null && root.right == null){
                root = null;
                return root;
            }

            //case 2: 1 child
            else if(root.left == null){
                //TreeNode tem = root;
                root = root.right;
                return root;
            } else if(root.right == null){
                root = root.left;
                return root;
            }

            //case 3: 2 childrens
            else{
                TreeNode tem = findMin(root.right);
                root.val = tem.val;
                root.right = deleteNode(root.right, tem.val);
            }
        }
        return root;
    }
    
    private TreeNode findMin(TreeNode root){
        while(root.left != null)
            root = root.left;
        
        return root;
    }
}