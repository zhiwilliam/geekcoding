class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def helper( left, right):
            if left > right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            idx = indexes[val]

            root.right = helper( idx +1, right  )
            root.left = helper(left, idx -1 )

            return root

        # enumerate(inorder)
        # indexes = { v:k for k,v in enumerate(inorder)}
        indexes = { }
        idx = 0
        for x in inorder:
            indexes[x] = idx
            idx += 1

        return helper(0, len(inorder)-1)
