
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        while root:
            if not root.left:
                root = root.right 
                continue 

            #find most right leaf for left sub-tree 
            pre = root.left 
            while pre.right: 
                pre = pre.right 
            
            pre.right = root.right 
            root.right = root.left 
            root.left = None 

            root = root.right 


