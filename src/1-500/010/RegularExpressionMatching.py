class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            dp[0][i] = p[i - 1] == '*' and dp[0][i - 2] and i > 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*': #当匹配字符串相应位置为星号（因为j从1开始，所以相应位置要减一）
                    #p字符为'*'时，则真值一定和去掉*及其前面的符号相同或者*前面的字符与s字符相同则让*填充一次真值保持与s之前的真值相同
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    # 前次字符串和匹配串匹配成功，双方同时比较下一个字符是否相同（点号也可以匹配成功）。
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == '.' or p[j - 1] == s[i - 1])
        return dp[len(s)][len(p)]


solution = Solution()
print(solution.isMatch("", "ab*"))
