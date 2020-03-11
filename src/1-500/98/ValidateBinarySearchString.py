class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min, max):
        if not root: return True
        if root.val >= max or root.val <= min:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)

