# 题目
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# 级别 
Easy

# 解题思路
At the moment, the only viable core strategy seems to be traversing `t` and ignoring letters that are not in `s` (please correct me if I'm wrong). Therefore, efficient solutions seem to focus on achieving that core strategy in the most efficient way.

A simple way to do this is through a loop that has a fast pointer and a slow pointer, using the fast pointer to traverse `t` and the slow pointer to traverse `s`, incrementing the fast one every loop and the slow one when the values referenced by both pointers are equal. However, this is not very efficient.

A more efficient way of doing this is by using Python's built-in iter() function and implicitly traversing `t`.

For both approaches, the time and space complexity is O(m+n) and O(1), respectively.
