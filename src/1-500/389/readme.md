# 题目
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

# 级别 
Easy

# 解题思路
The lower bound for the time complexity can be determined in a straight-forward way: We can't guarantee a result until we have looked at all the letters in `s` and `t`, so the best we can do is `O(m+n)`.  

There are multiple ways to go through the letters in both strings:
- Using two collections such as Counters or Hashmaps
- Sorting both strings and iterating through both at the same time
- Converting each letter to a unique numeric value and finding the difference between the sums and `s` and `t`

The last approach seems to be the most efficient in space complexity, since it is O(1) space.