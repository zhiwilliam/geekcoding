# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head 

        p = self.reverseList( head.next)
        head.next.next = head 
        head.next = None         ### IMPORTANT, otherwise LOOP link  
        return p 
