from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        from collections import deque
        queue = deque([(root.left, root.right)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.extend([(node1.left, node2.right), (node1.right, node2.left)])
        return True

    def isSymmetric_recr(self, root: TreeNode) -> bool:
        def isMirror(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and \
                   isMirror(node1.left, node2.right) and \
                   isMirror(node1.right, node2.left)
        return isMirror(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    print(solution.isSymmetric_recr(root))