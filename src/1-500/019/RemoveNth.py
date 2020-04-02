class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(0)
        root.next = head
        fast, slow, pre = root, root, root
        while n - 1:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return root.next


solution = Solution()
head = ListNode(1)
p = head
for i in range(2, 10):
    node = ListNode(i)
    p.next = node
    p = node

solution.removeNthFromEnd(head, 3)
p = head
while p:
    print(p.val)
    p = p.next