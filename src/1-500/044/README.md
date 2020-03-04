# 题目
## Trapping Rain Water
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

# 级别 
Hard

# 算法口号
动态规划，*号取决于它之前的match

# 解题思路
对于这种字符串+动态规划的题，题目问的是s和p是否匹配，我们应该把它认为是s的前len(s)个字符与p的前len(p)个字符是否匹配。这是一种对问题的不同层次的看法，用动态发展的眼光去看。既然动态规划，最难的就是研究动态转移方程，接下来剖析一下。

dp[i][j]表示p的前i个字符与s的前j个字符是否匹配。

# 算法归类
<a href="../../../DP.md">动态规划</a>
