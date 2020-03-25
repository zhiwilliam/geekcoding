class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        right, p = 0, head 
        while p:
            right += 1
            nums.append(p.val)
            p = p.next 

        def helper( left, right):
            if left > right:
                return None 
            mid = (left+right)//2 
            node = TreeNode(nums[mid])
            node.left = helper( left, mid-1)
            node.right = helper(mid+1, right)
            return node 

        return helper(0, right-1)
