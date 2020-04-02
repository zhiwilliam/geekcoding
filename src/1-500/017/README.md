# 题目
## Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

# 级别 
Medium

# 算法口号
回溯法

# 解题思路
依然是回溯法。要求所有的可能的字符串的组合。

有点类似784. Letter Case Permutation，不需要对index进行for循环，因为对index进行for循环产生的是所有可能的组合。而这两个题要求的组合的长度是固定的，每个位置都要有字母。

另外就是要判断一下path != ''，原因是当digits为“”的要求的结果是[]，而不是[“”]。