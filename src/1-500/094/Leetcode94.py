# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        inorder = []
        _inorder = inorder.append
        trace = []
        _trace = trace.append
        if root == None:
            return inorder
        current = root
        while True:
            if current is not None:
                _trace(current)
                current = current.left
            elif(trace):
                current = trace.pop()
                _inorder(current.val)
                current = current.right
            else:
                break
        return inorder

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(5)
    S = Solution()
    print(S.inorderTraversal(root))
