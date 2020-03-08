# 题目
Share
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

# 级别 
Easy

# 算法口号
Three pointers to solve three two-pointer problems

# 解题思路
Since we know it can be done in O(n) time and O(1) space, it should be done that way.  
The goal is to compare each pair of values in positions `n` and `len(list) - n`
Accessing a list item is O(n) time, so we cannot access the list for each comparison, and must traverse the list instead.  
There are 3 things we need to do:
1. We want to divide the list in half. This can be done most efficiently using two pointers, `slow` and `fast`.
2. We want to reverse one of the halves... (We can do this using two pointers, `slow` and `temp`, at the same time as step 1)
3. ... so we can traverse both halves and compare the values. (we can re-use `slow` and `temp` to traverse each half of the list)