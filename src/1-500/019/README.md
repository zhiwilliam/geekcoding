# 题目
## Remove Nth Node From End of List
删除一个单链表的倒数第n个节点。
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

# 级别 
Medium

# 算法口号
快慢指针，注意可能删除头节点

# 解题思路
先来分析一下这个题埋的坑吧。
第一，首先要判断这个n是不是有效，如果n超出链表长度怎么办，还好题目给了n是有效的。
第二，如果要删除头结点怎么办？估计很多人栽在了这个上面。这里很巧妙地自己定义了一个root节点
第三，题目说的是单链表没错，但是是否有环呢？当有环的时候，没有倒数第n个节点，你让我怎么办？很遗憾，题目没有说明这一点，我认为这是题目不严谨的地方。

具体到解法，这个题肯定是使用快慢指针啊，两个之间的距离是n，所以当快指针指向结尾的时候，慢指针正好指向了倒数第n个。因为要删除慢指针的位置，所以需要一个pre指针记录一下前面的那个节点的位置。

由于有可能删除首节点，所以使用哑结点当做新的头可以解决。