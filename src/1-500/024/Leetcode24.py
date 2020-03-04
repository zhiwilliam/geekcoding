import time
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
      pre = ListNode(None)
      pre, pre.next = self, head
      while pre.next and pre.next.next:
          a = pre.next
          b = a.next
          pre.next, b.next, a.next = b, a, b.next
          pre = a
      return self.next

if __name__ == '__main__':
  a = ListNode(1)
  a.next = ListNode(2)
  a.next.next = ListNode(3)
  a.next.next.next = ListNode(4)
  a.next.next.next.next = ListNode(5)
  a.next.next.next.next.next = ListNode(6)
  S = Solution()
  result = S.swapPairs(a)
  while result:
    print(result.val)
    result = result.next