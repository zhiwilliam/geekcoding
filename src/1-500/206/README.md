#  206 反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Solution

##  迭代

Ulitilize Python beautiful mulitple assignemnt to easy the job:

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None  
        while head:
###            head.next, pre, head = pre, head, head.next 

        return pre 


##  递归

Looks not as good as Loop/Iterative solution, not recommand.

    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head 

        p = self.reverseList( head.next)
        head.next.next = head 
        head.next = None         ### IMPORTANT, otherwise LOOP link  
        return p 


