# 题目
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

# 级别 
Hard

# 算法口号
掰开起首单词，剩下递归，递归找不到不加结果

# 解题思路
本题是上一题（139题）的改动题。我认为此一组题非常经典。当我们求一个合计的题的时候往往是用动态规划。
但是如果是求全部可能的集合，则往往不再用动态规划，而是用深度优先之类的算法。本题就是深度优先。
掰开字符串的首单词，
本题还使用了一个memo字典来存储已经成功处理过的字符串。对提高运行效率非常有用。

# 算法归类
<a href="../../../DFS.md">深度优先</a>