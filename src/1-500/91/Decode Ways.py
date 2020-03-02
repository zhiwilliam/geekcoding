class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == 0:
            return 0
        n = len(s)
        dp = [0 for i in range(n)]
        if s[0] != '0':
            dp[0] = 1
        for i in range(1, n):
            x = int(s[i])
            y = int(s[i - 1:i + 1])
            if 1 <= x <= 9:
                dp[i] += dp[i - 1]
            if 10 <= y <= 26:
                if i - 2 >= 0:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1
        return dp[-1]
