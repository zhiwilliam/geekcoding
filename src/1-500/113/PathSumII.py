from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ret = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            node, remind, path = stack.pop()
            if not node.left and not node.right and remind == 0:
                ret.append(path)
            if node.left:
                stack.append((node.left, remind - node.left.val, path + [node.left.val]))
            if node.right:
                stack.append((node.right, remind - node.right.val, path + [node.right.val]))
        return ret


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    solution = Solution()
    print(solution.pathSum(root, 22))