# 题目
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

# 算法口号


# 解题思路
创建head. 找到m的前一个节点-Pre 记录Pre的下一个节点，它会是翻转链的尾部。
翻转指定区间的链表，翻到最后一个节点时，把reverseTail.next指向它的next。这样就把翻转链表与之后 的链表接起来了。 返回dummynode的下一个节点
# 算法归类
<a href="../../../DataStructure.md"></a>
