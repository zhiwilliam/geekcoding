# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.sol2(l1, l2)
    
    def sol(self, l1, l2):
        if l1 == None and l2 == None:
            return l1
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        tmp_l1 = [l1.val]
        _tmp_l1 = tmp_l1.append
        tmp_l2 = [l2.val]
        _tmp_l2 = tmp_l2.append
        while l1.next:
            _tmp_l1(l1.next.val)
            l1 = l1.next
        while l2.next:
            _tmp_l2(l2.next.val)
            l2 = l2.next
        result = sorted(tmp_l1 + tmp_l2)
        _result = ListNode(result[0])
        self.constructLinkedList(_result, result[1:])
        return _result
    
    def sol2(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if (l1.val < l2.val):
            l1.next = self.sol2(l1.next, l2)
            return l1
        else:
            l2.next = self.sol2(l2.next, l1)
            return l2
    
    def constructLinkedList(self, l, result):
        if result == []:
            return None
        tmp = ListNode(result[0])
        l.next = tmp
        result.pop(0)
        return self.constructLinkedList(l.next, result)