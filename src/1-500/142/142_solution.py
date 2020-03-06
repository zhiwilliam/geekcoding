class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #龟兔赛跑问题
        #解题思路：龟node一次走一步，兔node一次走两步，如果龟兔撞上了，return true，else false
        if head == None:
            return None
        #single node
        dummy = ListNode(None)
        dummy.next = head
        
        tortoise = dummy
        hare = dummy
        
        while True:
            
            if(hare.next == None or tortoise.next == None):
                return None
            
            tortoise = tortoise.next
            hare = hare.next.next
            
            if(hare == None):
                return None
            
            if(tortoise == hare):
                break
                
        hare = dummy 
        while True:
            tortoise = tortoise.next
            hare = hare.next
            
            if(tortoise == hare):
                return hare
            
            
        return None