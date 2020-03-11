class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, running_sum = stack.pop()
            if not node.left and not node.right and running_sum == sum:
                return True
            if node.left:
                stack.append((node.left, running_sum + node.left.val))
            if node.right:
                stack.append((node.right, running_sum + node.right.val))
        return False

    def hasPathSum_recur(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum_recur(root.left, sum - root.val) or \
               self.hasPathSum_recur(root.right, sum - root.val)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    solution = Solution()
    print(solution.hasPathSum(root, 22))
    print(solution.hasPathSum_recur(root, 22))