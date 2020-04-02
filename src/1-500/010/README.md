# 题目
## Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

# 级别 
Hard

# 算法口号
动态规划 注意*号为0-n次匹配

# 解题思路
这题的动态规划思路是把这个问题转换成走迷宫看看走得出走不出的问题。

建立一个1+len(匹配串)， 1+len（字符串）的数组
0，0 代表字符串和匹配串都为空的情况
数组的第一行表示字符串为空的时候，匹配能否完成，也是一步步来，每一步都根据前一步的结果决定能否匹配。
记住*号是可以表示0次匹配（效果就是擦掉前一个匹配字符）所以第一个for对*号特别注意了。
然后是字符串逐渐加大，每一次都通过对前次匹配的结果再分本次是否为星号两条路径进行分析。
