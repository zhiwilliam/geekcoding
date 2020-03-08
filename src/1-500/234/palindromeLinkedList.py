# Three-pointer solution
# 1. use slow and fast to separate list in middle
# 2. use temp and slow to reverse first half
# 3. traverse both halves of the list using temp and slow, check if all pairs of values match

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        temp = None
        while fast and fast.next:
            fast = fast.next.next
            temp, temp.next, slow = slow, temp, slow.next
        if fast:
            slow = slow.next
        while temp and temp.val == slow.val:
            slow, temp = slow.next, temp.next
        return not temp