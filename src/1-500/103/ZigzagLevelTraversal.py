from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def zigzagLevelOrder_insert(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        res = []
        queue = deque([(root, 0)])
        direction = True

        while queue:
            res.append([])
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                if direction:
                    res[level].append(node.val)
                else:
                    res[level].insert(0, node.val)
            direction = not direction
        return res

    def zigzagLevelOrder_reverse(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        res = []
        queue = deque([(root, 0)])
        direction = True

        while queue:
            tmp = []
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                tmp.append(node.val)
            if direction:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            direction = not direction
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.zigzagLevelOrder_reverse(root))
    print(solution.zigzagLevelOrder_insert(root))