# 题目
## Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

# 级别 
Easy

# 算法口号
压栈出栈

# 解题思路
第一感觉就是栈，但是怎么用呢。这个方法就是如果左边的括号出现，那么把右边的括号放到栈里，这样，如果不是左边的括号出现时，弹出右边的括号，判断栈里边最后入的那个元素和目前的右边括号是否相同。如果不同就返回false。有种可能是入栈很多左括号，右括号个数小于左括号个数，所以最后也要判断一下栈是否为空，如果是空说明左右括号个数正好匹配。