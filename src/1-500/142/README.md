# 142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example1
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the second node.

![Example 1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

Example2


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)


Example2


Input:  head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

Result:
Success
Details 
Runtime: 52 ms, faster than 48.35% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.