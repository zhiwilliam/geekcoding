class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, start, end):
        newhead = ListNode(0)
        newhead.next = start
        while newhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp
        return [end, start]


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        root = ListNode(0)
        root.next = head
        start = root
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if not end.next: return root.next
            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return root.next


solution = Solution()
head = ListNode(1)
p = head
for i in range(2, 10):
    node = ListNode(i)
    p.next = node
    p = node

head = solution.reverseKGroup(head, 3)

p = head
while p:
    print(p.val, end=' ')
    p = p.next