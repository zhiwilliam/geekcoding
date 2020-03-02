# 题目
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

# 级别 
Easy

# 算法口号
It's a matter of iterating over the input efficiently, hence it's worthwhile to consider built-in functions that allows you to do this.

# 解题思路
The basic idea is iterating over a string of chars and a list of string, and looking for a one-to-one relationship between the values.  

My first solution uses a dictionary to hold the char-string pairs, and explicitly checking for mismatches every iteration.  

However, it's easier (as the alternative solutions demonstrate) to infer a one-to-one relationship using the built-in map() or zip(). Both approaches make sense, but the map() one satisfies my OCD the most since it does not require any other explicit checks.

# 算法归类
<a href="../../../DataStructure.md">Data Structure</a>
