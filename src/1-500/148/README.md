# 题目
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

# 级别 
Medium

# 算法口号
左右递归快慢指针分链表再merge排好的链表，

# 解题思路
把链表一分为二，然后再左右链表merge sort。快慢指针分链表要背一下，常用。merge sort没啥难度。看看递归怎么弄。

# 算法归类
<a href="../../../DataStructure.md">数据结构（链表）</a>