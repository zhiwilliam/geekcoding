from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, res, wordDict, memo):
            if s in memo:
                return memo[s]
            if not s:
                return [""]
            res = []
            for word in wordDict:
                if s[:len(word)] != word: continue # 如果字符串开头的单词找不到，就跳过了。
                for r in dfs(s[len(word):], res, wordDict, memo): # 如果找到了，那么剩下的字符串递归再求解。注意数组如何切分，如果没找到，不动res
                    res.append(word + ("" if not r else " " + r)) # 处理空字符串
            memo[s] = res
            return res
        res = []
        memo = {}
        return dfs(s, res, wordDict, memo)



solution = Solution()
#print(solution.wordBreak("aab", ["aa"]))
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
