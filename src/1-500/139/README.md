# 题目
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

# 级别 
Medium

# 算法口号
dp数组存是否能分割，注意dp[0] = True

# 解题思路
动态规划（dp）题。其实就是从第一个字符开始，不断重复扫描，如果全部可分就存入True。
什么叫全部可分？就是添加了一个字符以后，这个字符往前看，可以看到一个字典里有的单词。
然后如果这个词之前的字符串依然可全分（在程序里dp[k]为True），那么就认为它是全可分的。
最后的结果是看最后一个是不是True

# 算法归类
<a href="../../../DP.md">动态规划</a>