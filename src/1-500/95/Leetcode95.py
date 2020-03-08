# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.constructBST(1, n)

    def constructBST(self, head, n):
        if (head > n):
            return [None]
        result = []
        _result = result.append
        for i in range(head, n + 1):  # i as root for every item in range(n)
            leftSubtree = self.constructBST(head, i - 1)
            rightSubtree = self.constructBST(i + 1, n)
            for j, left in enumerate(leftSubtree):
                for k, right in enumerate(rightSubtree):
                    right = rightSubtree[k]
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    _result(node)
        return result
