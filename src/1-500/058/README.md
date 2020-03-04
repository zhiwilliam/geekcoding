# 题目
## Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
             
# 级别 
Eazy

# 算法口号
从后往前查，注意空格处理

# 解题思路
这道题不难，从后往前查。设一个计数器，如果是空格且计数器为零，则跳过。如果不是空格，计数器加。如果是空格且已经计数就返回了。<br>

这题请看一下python怎么用for来倒序的。不用while的原因是容易错。我continue之前忘了把index - 1结果就错了。