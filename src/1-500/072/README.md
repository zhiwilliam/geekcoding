# 题目
## Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

# 级别 
Hard

# 算法口号
动态规划

# 解题思路
开一个二维数组，长宽分别是两个输入字符串长度+1。

第一行和第一列的值分别表示如果另一个字符串为空，那么形成本字符串需要几次变化？当然就是1，2，3，4...

然后，每一格如果x，y相同，那么就不需要变换，直接照抄x-1，y-1位置的结果。否则取不同路径（代表三种变换）中较小的那个。