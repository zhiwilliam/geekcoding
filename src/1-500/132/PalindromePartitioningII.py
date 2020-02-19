import sys


class Solution:
    def minCut(self, s: str) -> int:
        if not s: return
        l = len(s)
        dp, rst = [[0] * l for _ in range(l)], [sys.maxsize for _ in range(l + 1)]
        rst[0] = -1
        for j in range(l):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    rst[j + 1] = min(rst[j + 1], rst[i] + 1)  # 最优解
        return rst[-1]


solution = Solution()
print(solution.minCut("aab"))