# 112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note**: A leaf is a node with no children.

**Example**:

Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# 分析
这道题要求判断是否存在一条从树根到叶子的路径，使得这条路径上的数字总和是题目要求的数字。这是一道典型的深度优先算法的题。同时这道题也可以用递归的方法来做。
## 1. 深度优先（BFS）
```Python
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
```
## 2. 递归
```Python
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    return self.hasPathSum(root.left, sum - root.val) or \
            self.hasPathSum(root.right, sum - root.val)
```