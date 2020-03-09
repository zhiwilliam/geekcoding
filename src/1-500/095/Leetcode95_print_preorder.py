# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []
        self.tmp = []

    def generateTrees(self, n):
        if n == 0:
            return []
        return self.constructBST(1, n)

    def constructBST(self, head, n):
        result = []
        if (head > n):
            return [None]
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

    def preorderTraversal(self, root):
        if (root != None):
            self.tmp.append(root.val)
            if root.left:
                self.preorderTraversal(root.left)
            else:
                self.tmp.append('{} has no left child'.format(root.val))
            if root.right:
                self.preorderTraversal(root.right)
            else:
                self.tmp.append('{} has no right child'.format(root.val))


if __name__ == '__main__':
    S = Solution()
    allTrees = S.constructBST(1, 3)
    for tree in allTrees:
        S.preorderTraversal(tree)
        print(S.tmp)
        S.result.append(S.tmp)
        S.tmp = []
