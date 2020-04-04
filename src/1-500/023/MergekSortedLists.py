import heapq
from functools import total_ordering
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val <= other.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(-1)
        move = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, l)) for i, l in enumerate(lists) if l]
        while heap:
            curVal, curHead = heapq.heappop(heap)
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            if curHead:
                heapq.heappush(heap, (curHead.val, curHead))
        return head.next


def mkList(list: List[int])->ListNode:
    root = ListNode(0)
    node = root
    for i in list:
        node.next = ListNode(i)
        node = node.next
    return root.next
solution = Solution()
node = solution.mergeKLists([mkList([1, 4, 5]), mkList([1, 3, 4]), mkList([2, 6])])
while node:
    print(node.val, end=' ')
    node = node.next