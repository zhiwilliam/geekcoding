class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        # 经典的快慢指针查中点。
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        righthalf = slow.next
        slow.next = None

        # 三指针 reverse 链表 非递归版本
        prev, curr = None, righthalf
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # 双链表的merge，注意while的条件是move 2指针不为空。原因在于奇数中点归了后半条。
        mv1 = head
        mv2 = prev
        while mv2:
            tmp = mv1.next
            mv1.next = mv2
            mv1 = tmp
            tmp = mv2.next
            mv2.next = mv1
            mv2 = tmp


points = [1, 2, 3, 4, 5]
head = ListNode(points[0])
node = head
for i in range(1, len(points)):
    node.next = ListNode(points[i])
    node = node.next


def printNode(head: ListNode):
    print(head.val)
    if head.next:
        printNode(head.next)

solution = Solution()
solution.reorderList(head)
printNode(head)