from typing import List


class Solution:
    def backtrack(self, result, trace, path, word):
        if len(trace[word]) == 0:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)

    def findLadders(self, start: str, end: str, dict: List[str]) -> List[List[str]]:
        result, trace, current = [], {word: [] for word in dict}, set([start])
        while current and end not in current:
            for word in current:
                dict.remove(word)
            next = set([])
            for word in current:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate in dict:
                            trace[candidate].append(word)
                            next.add(candidate)
            current = next
        if current:
            self.backtrack(result, trace, [], end)
        return result

# class Solution:
#     def __init__(self):
#         shortest = 10000
#
#     def canChange(self, fromWord: str, toWord: str):
#         count = 0
#         for i in range(len(fromWord)):
#             if fromWord[i] != toWord[i]:
#                 count += 1
#         return count == 1
#
#     def help(self, currentWord: str, endWord: str, wordList: List[str], layer: int) -> List[List[str]]:
#         lists = []
#         if len(wordList) == 0 and layer > self.shortest:
#             return lists
#
#         for i in range(len(wordList)):
#             nextWord = wordList[i]
#             if self.canChange(currentWord, nextWord):
#                 if nextWord == endWord:
#                     shortest = layer
#                     return [[currentWord, endWord]]
#                 else:
#                     nextList = wordList.copy()
#                     nextList.remove(nextWord)
#                     results = self.help(nextWord, endWord, nextList, ++ layer)
#                     for result in results:
#                         result.insert(0, currentWord)
#                         lists.append(result)
#         return lists
#
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         if endWord not in wordList:
#             return None
#         else:
#             return [y for y in self.help(beginWord, endWord, wordList, 0) if len(y) == self.shortest]


beginWord = "hot"
endWord = "dog"
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
solution = Solution()

for result in solution.findLadders(beginWord, endWord, wordList):
    print(result)
