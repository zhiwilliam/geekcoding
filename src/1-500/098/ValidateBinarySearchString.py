from typing import List


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


def helper(input: List, i: int) -> TreeNode:
    if i < len(input) and input[i] is not None:
        node = TreeNode(input[i])
        node.left = helper(input, i * 2 + 1)
        node.right = helper(input, i * 2 + 2)
        return node
    else:
        return None


solution = Solution()
print(solution.isValidBST(helper([5,1,4,None,None,3,6], 0)))