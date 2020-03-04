# 题目
## Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

# 级别 
Medium

# 算法口号
把每一个字符串排序放字典

# 解题思路
这题真无聊。就是排序字符串放字典。没有啥好办法。
注意字符串排序的写法 ''.join(sorted(str))

# 算法归类
<a href="../../../DataStructure.md">数据结构</a>