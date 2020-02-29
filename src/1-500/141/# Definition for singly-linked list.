# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        #龟兔赛跑问题
        #解题思路：龟node一次走一步，兔node一次走两步，如果龟兔撞上了，return true，else false
        if head == None:
            return False
        #single node
        dummy = ListNode(None)
        dummy.next = head
        
        tortoise = dummy
        hare = dummy
        
        while True:
            
            if(hare.next == None or tortoise.next == None):
                return False
            
            tortoise = tortoise.next
            hare = hare.next.next
            
            if(hare == None):
                return False
            
            if(tortoise == hare):
                return True