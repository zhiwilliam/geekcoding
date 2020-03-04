86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

--------------------------------

Idea:

Use space to trade for time - Construct two separate linked lists to hold elements smaller and greater. Once finished, concatenate these two list into one.


--------------------------------

Runtime: 0 ms, faster than 100.00% of Java online submissions for Partition List.
Memory Usage: 38.3 MB, less than 5.77% of Java online submissions for Partition List.

--------------------------------

