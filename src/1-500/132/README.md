# 题目
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# 级别 
High

# 算法口号
用二维数组存字符串i到j是不是回文，遍历所有的i，j

# 解题思路
本题请参考上一题（131题）的解法

不同之处是131题输出所有的切法，而本题只需要输出最优的切法切几刀。这道题更符合DP题的样式，墙裂推荐掌握。

# 算法归类
<a href="../../../DP.md">动态规划</a>