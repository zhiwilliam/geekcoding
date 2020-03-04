82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

--------------------------------

Idea:

Since the target list is sorted, only one place holder is needed to hold previous value. 
While looping on current pointer, advance current as long as duplicates are found, then check if any duplicate has been identified - if so, move prev next pointer to curr next so that duplicates are by-passed; otherwise, advance prev and curr by just one position.


--------------------------------

Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 39.2 MB, less than 6.98% of Java online submissions for Remove Duplicates from Sorted List II.

--------------------------------

