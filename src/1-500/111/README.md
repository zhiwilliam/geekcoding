# 111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note**: A leaf is a node with no children.

## Example:

Given binary tree [3,9,20,null,null,15,7],

      3
     / \
    9  20
       /  \
      15   7
return its minimum depth = 2.
# 分析
这道题可以用BFS或者DFS来做。
## 1. BFS
BFS的思路是一层层遍历，当你找到第一片叶子的时候，就已经找到最小的深度了。
<img src="tree.png">

如上图的例子中，我们用BFS算法一层层遍历，当遍历到第三层时，当遇到节点7或者20，这两个都是叶子，我们就直接返回它的层次数，在这个例子中是3。
### 代码：
```Python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
```
## 2. DFS
DFS的思路略有不同，我们的思路是走完每一条可以走的路径，然后返回最短的那条的长度。为了提前效率，如果我们遇到一条明显无效的，也就是说明显比我们之前找到的路径长的，我们应该能跳过这条路径。举例来说，我们目前找到的最短的是长度是4，当然这个长度不一定是最后的结果。我们现在走的路径当走的深度为4后，还没有尽头，那么至少说明这长路的长度比我们当前找到的最短的路径长度要长，不是我们想要的，于是我们要跳过这个树枝。
### 代码
```Python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = float('inf')
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                depth = min(depth, level)
            if level < depth:
                if node.left:
                    stack.append((node.left, level+1))
                if node.right:
                    stack.append((node.right, level+1))
        return depth
```

## 