# 题目
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

# 级别 
Easy

# 算法口号
Use a Counter for the magazine

# 解题思路
We can use a dictionary-type structure such as Counter or HashMap to counter the appearance of each letter in the magazine, then iterate over the ransom note to check each letter (assuming the ransom note is much shorter than the magazine).  

Interestingly enough, the 3 approaches all run at a similar time based on a test case with a 13-letter ransom note and a 170,000-letter magazine. Even with a loop that uses count() on both the note and the magazine each loop, the performance is similar.  

It looks like Python is doing something under the hood here.

Time Complexity: O(m+n)
Space Complexity: O(m+n)