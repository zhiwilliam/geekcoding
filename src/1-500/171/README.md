# 题目
## Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701





# 解题思路
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
>>>ord('a')
97
>>> ord('b')
98
>>> ord('c')
99

A  = 1
Z  = 26
AA = 27 26*1 + 1
AZ = 52 26*1 + 26
BA = 53 26*2 + 1
BZ = 78 26*2 + 26
AAA  = 26*26*1 + 26*1 + 1
ZAA  = 26*26*26 + 26*1 + 1


Writing these out helped me to see the pattern - do you see it?
Essentially, we can. rewrite them as:

AAA  = 26^2*1 + 26^1*1 + 26^0
ZAA  = 26^2*26 + 26^1*1 + 26^0
So we simply have to reverse s, and iterate through it since we want the last character to be raised to the power of i where i is ranged 0 to 25. And we can multiply by the mapping of each character using ord(s[i]) - 64, deriving from ASCII values.

def titleToNumber(self, s: str) -> int:
	return sum([26**i*(ord(c)-64) for i,c in enumerate(s[::-1])])

# 算法归类
Math
