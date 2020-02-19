from typing import List

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return
        l = len(s)
        dp, rst = [[0] * l for _ in range(l)], [[] for _ in range(l + 1)]
        rst[0].append([])
        for j in range(l):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    apal = s[i:j + 1]
                    for lst in rst[i]:
                        rst[j + 1].append(lst + [apal])
        return rst[-1]


solution = Solution()
print(solution.partition("aab"))


