class Solution:
    def connect(self, root: 'Node') -> 'Node':
        veryLeftOfCurrentLevel = root 
        while veryLeftOfCurrentLevel:
            currNode = veryLeftOfCurrentLevel
            while True :
                if currNode.left:  # not the leaf node 
                    currNode.left.next = currNode.right 

                if not currNode.next: # the very right node 
                    break 
                
                if currNode.right:  # not the leaf node 
                    currNode.right.next = currNode.next.left 

                currNode = currNode.next        

            veryLeftOfCurrentLevel = veryLeftOfCurrentLevel.left 

        return root 
