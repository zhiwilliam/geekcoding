# 题目
## Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# 难度
Medium

# 算法口号
字典char index。记录每一段的start位置。最后不要忘了计算corner case

# 解题思路
用一个字典记录每一个字符的最后出现位置。如果start的位置小于新出现的重复数字原来所在的位置，就要计算当前位置与start位置之间的距离，看看是不是最大的距离，然后把start移动到重复数字之后的一位。

