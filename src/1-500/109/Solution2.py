class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None 
        
        def findMid(head:ListNode) -> ListNode:
            pre, slow, fast = head, head, head 
            while fast.next and fast.next.next:
                pre, slow, fast = slow, slow.next, fast.next.next 
            if pre != slow:
                pre.next = None 
            return slow 
        
        mid = findMid(head)
        root = TreeNode(mid.val)

        if mid != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root 
