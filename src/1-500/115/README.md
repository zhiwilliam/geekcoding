# 题目
## Distinct Subsequences
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
    
# 级别 
Hard

# 算法口号
动态规划

# 解题思路
这道题和74题非常接近。

设dp数组dp[i][j]表示S的前j个字符是T的前i个字符的子序列的个数为dp[i][j]。

那么有dp[0][*] == 1，因为这个情况下，只能使用s的空字符串进行匹配t。

如果s[j - 1] == t[i - 1]，那么，dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]，原因是t的前j个字符可以由s的前[i - 1]个字符和t的前[j - 1]个匹配的同时最后一个字符匹配，加上s的前[j - 1]个字符和t的前[i]个字符匹配同时丢弃s的第[j]个字符。

如果s[j - 1] != t[i - 1]，那么dp[i][j] = dp[i][j - 1]，因为只能是前面的匹配，最后一个字符不能匹配，所以丢弃了。

