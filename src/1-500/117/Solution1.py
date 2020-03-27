from collections import deque 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque([root])
        while q:
            pre = None 
            for _ in range(len(q)):
                node = q.popleft()
                if pre:
                    pre.next = node 
                pre = node 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root 
