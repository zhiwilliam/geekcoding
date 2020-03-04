class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        pre = head
        cut = head
        # 先移动到要求的间隙
        count = 0
        i = 0
        while i < k:
            cut = cut.next
            count += 1
            i += 1
            if not cut:
                cut = head
                i = 0
                k = k % count

        if cut == pre: return head

        # 然后两指针一块儿移动，直到cut 撞到最后一个node
        while cut.next:
            pre = pre.next
            if not pre.next:
                pre = head
            cut = cut.next

        # 在这个地方break，连到head上。
        newHead = pre.next
        pre.next = None
        cut.next = head
        return newHead


head = ListNode(0)
pre = head
for i in range(1, 3):
    node = ListNode(i)
    pre.next = node
    pre = node
mv = head
while mv:
    print(str(mv.val) + "->", end = ""),
    mv = mv.next

print("None")
solution = Solution()
res = solution.rotateRight(head, 24)

while res:
    print(str(res.val) + "->", end = ""),
    res = res.next
print("None")
