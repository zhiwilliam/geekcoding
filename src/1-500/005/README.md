# 5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

```python
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
```

#Analysis
Expand from the center, and check if it' Palindrome, using a variable to keep tracking the longest length

#Source Code
```java
class Solution {
    //expande from the center
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        int start = 0; // keep the index to remember to start of the substring 
        int end = 0; // and the end of the substring
        int maxLen = 0;
        String ans = "";
        for(int i = 0; i < s.length(); i++) {
            int len1 = expandFromCenter(s, i, i);
            int len2 = expandFromCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (maxLen < len) {
                maxLen = len;
                ans = s.substring(i - (len - 1) / 2, i + len / 2 + 1 ); // here is tricky
            }
        }
        return ans;
    }
    
    private int expandFromCenter(String s, int left, int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
``` 