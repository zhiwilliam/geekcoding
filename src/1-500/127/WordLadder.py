import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0

beginWord = "hot"
endWord = "dog"
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
solution = Solution()

print (solution.ladderLength(beginWord, endWord, wordList))
