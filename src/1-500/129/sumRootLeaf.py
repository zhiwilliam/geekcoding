from typing import List


class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node: TreeNode, num: List[str]) -> None:
            # Gather integers using list of characters
            num.append(str(node.val))
            # If leaf, convert list into string and then to integer and then add the integer to the result
            if not node.left and not node.right: self.result += int("".join(num))
            # num[:] passes list not by reference
            if node.left: helper(node.left, num[:])
            if node.right: helper(node.right, num[:])

        # Edge case
        if not root: return 0
        self.result = 0
        helper(root, [])
        return self.result

# 解法II
# class Solution:
#     def sumNumbers(self, root: TreeNode) -> int:
#         def help(node: TreeNode) -> List[List[int]]:
#             if node is None:
#                 return []
#
#             values = help(node.left) + help(node.right)
#             if len(values) == 0:
#                 return [[node.val]]
#             else:
#                 for x in values:
#                     x.insert(0, node.val)
#
#             return values
#
#         valuesList = help(root)
#         total = 0
#         for values in valuesList:
#             result = 0
#             for value in values:
#                 result = result * 10 + value
#
#             total += result
#         return total



def helper(input: List, i: int) -> TreeNode:
    if i < len(input) and input[i] is not None:
        node = TreeNode(input[i])
        node.left = helper(input, i * 2 + 1)
        node.right = helper(input, i * 2 + 2)
        return node
    else:
        return None

tree = helper([4, 9, 0, 5, 1], 0)
solution = Solution()
print(solution.sumNumbers(tree))