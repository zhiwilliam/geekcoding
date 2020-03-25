class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None 

        #calc the length of the linked list 
        len, node = 0, head 

        while node:
            len += 1 
            node = node.next 

        def convert( start, end  ):

            nonlocal head 

            if start > end:
                return None 

            mid = (start + end)//2
            left = convert( start, mid-1)

            node = TreeNode(head.val)
            node.left = left 

            head = head.next 

            node.right = convert(mid+1, end)
            return node 

        return convert(0, len-1)

