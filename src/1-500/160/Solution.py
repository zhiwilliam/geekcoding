class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA, currB  = headA , headB 
        while currA != currB:
            currA = currA.next  if currA else headB 
            currB = currB.next  if currB else headA 
        return currA 

