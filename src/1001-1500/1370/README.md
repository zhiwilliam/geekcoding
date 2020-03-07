# 题目
## Increasing Decreasing String
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

# 题目简介
其实就是一个字符串里出现的所有字符先从小往大打印，再从大往小打印。

# 级别 
Easy

# 算法口号
数组存所有字符出现的次数，然后从左往右，从右往左扫描数组

# 解题思路
这道题是典型的字符串操作题。它利用了英文字母只有26个的特性。

先开一个26个空格的数组，代表了英文26个字母的现后顺序。
然后扫描输入的字符串，出现的每一个字符，都通过减去a的ascii码转换成数组的index。把相应位置的数字加1
全部扫完后，我们就知道每一个字符出现的次数了。然后从左往右扫描存储数组，只要index大于0就把值加到返回数组中
。再从右往左扫，以此类推，知道所有字符都加到了返回字符串，最后返回生成的新字符串。