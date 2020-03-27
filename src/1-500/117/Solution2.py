class Solution:
    def findNextChild(self,root):
        while root.next:
            root = root.next 
            if root.left:
                return root.left 
            if root.right:
                return root.right 
        return None 


    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        if not root or ( not root.left and not root.right):
            return root 

        if root.left and root.right:
            root.left.next = root.right 
            root.right.next = self.findNextChild(root)

        if not root.left:
            root.right.next = self.findNextChild(root)

        if not root.right:
            root.left.next = self.findNextChild(root)

        self.connect(root.right)
        self.connect(root.left)
        
        return root         
