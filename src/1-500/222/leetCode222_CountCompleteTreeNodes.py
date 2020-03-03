# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        # if left tree hight = right tree hight = h,  then it has 2^h - 1 nodes 
        # if not, then recursive 
        hL = self.hightLeft( root.left)
        hR = self.hightRight( root.right)
        if hL == hR :
            return 2**(hL + 1) - 1 
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 

    def hightLeft(self, root: TreeNode) -> int:
        h = 0 
        
        if not root:
            return h 
        while root.left:
            h += 1 
            root = root.left 
        
        return h + 1 
     
    def hightRight(self, root: TreeNode) -> int:
        h = 0 
        
        if not root:
            return h 
        while root.right:
            h += 1 
            root = root.right 
        
        return h + 1
