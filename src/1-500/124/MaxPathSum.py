from typing import List
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxValue = -10000000

    def help(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.help(root.left)
        right = self.help(root.right)
        child = max(left, right)
        if child > 0:
            # 注意这里序要比较三个值，儿子的最大值，过桥值还有儿子最大值加自己本身的值
            maxVal = max(child, left + right + root.val, child + root.val)
            if self.maxValue < maxVal:
                self.maxValue = maxVal
            return child + root.val
        else:
            maxVal = root.val
            if self.maxValue < maxVal:
                self.maxValue = maxVal
            return maxVal

    def maxPathSum(self, root: TreeNode) -> int:
        self.help(root)
        return self.maxValue


# This help can generate a tree from array.
def helper(input: List, i: int) -> TreeNode:
    if i < len(input) and input[i] is not None:
        node = TreeNode(input[i])
        node.left = helper(input, i * 2 + 1)
        node.right = helper(input, i * 2 + 2)
        return node
    else:
        return None

#inputList = [-10, 9, 20, None, None, 15, 7]
inputList = [-3]
node = helper(inputList, 0)
solution = Solution()
solution.maxPathSum(node)
print(solution.maxValue)

