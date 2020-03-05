# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off. -- Max Howell

# Recursive
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root

# Recursive after a hint to make code more elegant
    def invertTreePretty(self, root: TreeNode) -> TreeNode:
        if root != None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# Iterative
    def invertTreeIterative(self, root: TreeNode) -> TreeNode:
        if root != None:
            q = [root]
            while len(q) > 0:
                current = q.pop()
                current.left, current.right = current.right, current.left                
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q.append(current.right)
        return root
