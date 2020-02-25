from functools import reduce

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next:
            return '%s, %s' % (self.value, self.next)
        return '%s' % self.value


class Solution:
    def addThreeNumbers(self, num0: Node, num1: Node, num2: Node, newList: Node) -> Node:
        if num1 is None and \
                num2 is None and \
                num0 is None:
            return 

        value = ( num0.value if num0 is not None else 0 ) + \
                ( num1.value if num1 is not None else 0 ) + \
                ( num2.value if num2 is not None else 0 )
        newNode = Node(value % 10)
        newList.next = newNode

        incNode = Node(value//10) if value // 10 != 0 else None

        self.addThreeNumbers(
            incNode,
            num1.next if num1 is not None else None,
            num2.next if num2 is not None else None,
            newNode)

    def addTwoNumbers(self, num1: Node, num2: Node) -> Node:
        res = Node(-1)
        self.addThreeNumbers(None, num1, num2, res)
        return res.next


if __name__ == '__main__':
    nums1 = [2, 7, 6, 5]
    nums2 = [2, 7, 7, 5]

    def bindNode(pre, num):
        node = Node(num)
        pre.next = node
        return node

    ns1 = Node(-1)
    reduce(bindNode, nums1, ns1)
    ns1 = ns1.next

    ns2 = Node(-1)
    reduce(bindNode, nums2, ns2)
    ns2 = ns2.next

    res = Solution().addTwoNumbers(ns1, ns2)
    print('ns1: ', ns1)
    print('ns2: ', ns2)
    print('res: ', res)
