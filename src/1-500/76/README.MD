# 76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# 解题思路：
找到一个符合题目条件的Substring之后不断缩短这个Substring，直到找到临界点，

这个题目是典型的双指针题，我们解这个题的时候，要用到两个指针，一个叫快指针， 一个叫慢指针。在一开始搜索字符串S的时候，这两个指针都指向0，也就是S字符串开始的位置，然后向右移动快指针，每次移动之后都要判断从慢指针到快指针之间的S的子串是不是包含T中所有的字符。如果是，那么我们要开始移动慢指针，每次移动后都要再判断新的子串是不是还满足条件，如果是，把开始位置和长度记录下来。当我们移动慢指针后，子串不再满足条件了，我们就可以再次移动快指针。我们循环做这个移动指针，判断，直到S的结尾处。

为了方便，我们还需要几个变量，一个用来记录最短的Substring的开始位置，一个用来表示最短的Substring的长度。一个用来记录在当前时刻我们的程序已经Match了几个字符。最重要的是，我们需要一个Map来记录我们需要Match的字符。

# 注意事项
1. 题目中没有说t中的字符是distinct的，要考虑有重复的情况
2. edge cases:
   * 当t比s还要长的时候，直接返回一个空字符串
   * 当t或者s为空的时候，也直接返回空字符串

# 例子


<img src="leetcode76.png">

