# 题目
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# 级别 
Medium

# 算法口号
快慢指针，三指针算法

# 解题思路
这道题是把经典的链表操作合三为一了。第一段是查找链表中点，用快慢指针跑。注意while条件。
第二段是链表反转，经典的三指针问题。第三段是链表归并。

# 算法归类
<a href="../../../DataStructure.md">数据类型（链表）</a>