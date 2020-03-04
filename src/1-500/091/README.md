# 题目
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# 算法口号


# 解题思路
用传统DP解题思路，根据S的长度先从1位数截取,然后一直到s长度，介于字母只有26个，最多每次截取小于等于2位切大于等于1小于等于26

# 算法归类
<a href="../../../DataStructure.md">DP</a>
