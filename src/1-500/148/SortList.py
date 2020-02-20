class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        head = ListNode(0)
        move = head
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)
        return self.mergeTwoLists(l1, l2)

arr = [2, 1, 5, 3, 4]
head = ListNode(0)
mv = head
for v in arr:
    mv.next = ListNode(v)
    mv = mv.next

solution = Solution()
res = solution.sortList(head.next)
while res:
    print(res.val)
    res = res.next
