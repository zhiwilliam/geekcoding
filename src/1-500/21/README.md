题目
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

级别
Easy

解题思路
用Recursive迭代，每个步骤比较一次大小，拥有较小值的node安插在结果中返还
也可以用while loop来强行brute force解，不过两种办法在Leetcode当中报告为performance差不多
