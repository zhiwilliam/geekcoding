# 113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note**: A leaf is a node with no children.

**Example**:

Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
Return:
```Python
[
   [5,4,11,2],
   [5,8,4,5]
]
```
# 分析
这道题可以看作是112题的扩展。我们可以用类似的方法来做，要引入一个新的List来记录当前的路径，当遇到符合条件的路径时，我们将这个List加入到结果中。
```Python
def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    if not root:
        return []
    ret = []
    stack = [(root, sum - root.val, [root.val])]
    while stack:
        node, remind, path = stack.pop()
        print(id(path))
        if not node.left and not node.right and remind == 0:
            ret.append(path)
        if node.left:
            stack.append((node.left, remind - node.left.val, path + [node.left.val]))
        if node.right:
            stack.append((node.right, remind - node.right.val, path + [node.right.val]))
    return ret
```