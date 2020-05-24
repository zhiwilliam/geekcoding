### [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

难度:**中等**

给定一个字符串，逐个翻转字符串中的每个单词。

**示例 1：**

**输入:** "`the sky is blue`"
**输出:** "`blue is sky the`"

**示例 2：**

**输入:** "  hello world!  "
**输出:** "world! hello"
**解释:** 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

**示例 3：**

**输入:** "a good   example"
**输出:** "example good a"
**解释:** 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

**说明：**

-   无空格字符构成一个单词。
-   输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
-   如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


### Solution

(1) Use native function **split** to get the words in string, then reverse them before re-connecting them by space.

``` python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ret = words[::-1]
        return ' '.join(ret)
```

执行结果： 通过

执行用时 :44 ms, 在所有 Python3 提交中击败了58.66%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了10.00%的用户
 
(2) Do not use navite functions
``` python
class Solution:
    def reverseWords(self, s: str) -> str:

        #不能用split, trim, stringbuilder, 等function, 只能inplace 修改

        if not s :
            return s 

        words = []
        leftIndex, rightIndex = 0,0
        while leftIndex < len(s):
            while leftIndex < len(s) and  s[leftIndex] == ' ':
                leftIndex += 1 
            if leftIndex == len(s):
                break 
            rightIndex = leftIndex + 1 
            while rightIndex < len(s) and s[rightIndex] != ' ':
                rightIndex += 1 
            
            words.append(s[leftIndex:rightIndex])
            # print('s[{},{}]:"{}"'.format( leftIndex,rightIndex
            #             , s[leftIndex:rightIndex]))
            leftIndex = rightIndex + 1 
        if not words:
            return ''
        ret = words.pop()
        while words:
            w = words.pop()
            ret = ret + ' ' + w 
 
        return ret
```



