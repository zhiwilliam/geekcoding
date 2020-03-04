# 题目
## Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

# 级别 
Medium

# 算法口号
两字符串倒序，结果从最后往前填

# 解题思路
这题我觉得也挺难的。当场想不容易想出来，大家最好稍微背一下
```
res[tempPos] += int(n1) * int(n2)
res[tempPos - 1] += res[tempPos] // 10  # 进位
res[tempPos] %= 10  # 取余
```
这三句是关键，它是把乘法的结果先存在当前位，然后把十位上的数字填在前一格。本格再用余数填。
```
res = [0] * (len(num1) + len(num2))
```
这句开数组是保证不会溢出，但是最后要清0.
```
''.join(map(str, res[st:]))
```
最后这句从list转换成string非常有意思。我还没怎么看懂，请大佬指教

# 算法归类
<a href="../../../DataStructure.md">数组结构</a>