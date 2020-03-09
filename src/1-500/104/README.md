# 104. Maximum Depth of Binary Tree

这道题可以考虑111题中的分析。这里就不具体说了。
## 代码
```Python
# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = float('-inf')
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                depth = max(depth, level)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return depth
```