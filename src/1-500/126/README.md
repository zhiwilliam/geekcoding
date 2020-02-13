# 题目
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# 算法口号
宽度优先，建立全字典

# 解题思路
Create a trace dictionary
Start from start word, find all of possible changeable words in the list, put them to next layer.
Loop until find the end word ***while current and end not in current:***
if changeable words are found, remove them from list

Finally, when we found the end word in current layer, we use backtrace method to recreate the whole path.
Notes: trace dictionary includes all possible path you can reach. But no duplicated path. 
That's why you need to remove found changeable from the original list.

# 算法归类
<a href="../../../BSF.md">宽度优先搜索</a>