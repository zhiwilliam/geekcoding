# 数组和链表

链表的快慢指针找中点
```
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
```
