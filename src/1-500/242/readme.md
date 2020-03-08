# 题目
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

# 级别 
Easy

# 算法口号
Think about how a bucket sort works

# 解题思路
Whenever the number of different items are sufficiently small, it's worthwhile to think about using a bucket sort.  
Using a dictionary to count the number of appearances of each item is how a bucket sort starts, but since we don't need to finish the sort before we can compare the values, we won't.  
We could have used two dictionaries or just one, the idea is the same: each item should have the exact same number of appearances in both strings.
This approach should handle unicode characters nicely since a dicionary's performace should not increase with the number of keys.