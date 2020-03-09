class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # iterate all nodes, remove if matches

        dummyNode = ListNode(0)
        dummyNode.next = head 

        preNode = dummyNode
        currNode = head 
        while currNode:
            #print(currNode.val)
            if currNode.val == val:
                preNode.next = currNode.next 
            else:
               preNode = currNode

            currNode = currNode.next 

        return dummyNode.next 

