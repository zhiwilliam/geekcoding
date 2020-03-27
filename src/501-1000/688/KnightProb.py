class Solution:
    def knightProbability_dp(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0.0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1.0
        dirs = [(-2, 1), (-2, -1), (1, -2), (1, 2),
                (2, 1), (2, -1), (-1, 2), (-1, -2),]
        for k in range(K):
            dp_temp = [[0.0 for _ in range(N)] for _ in range(N)]
            for x in range(N):
                for y in range(N):
                    for dx, dy in dirs:
                        if 0 <= x + dx <= N-1 and 0 <= y + dy <= N-1:
                            dp_temp[x][y] += dp[x + dx][y + dy] / 8
            dp = dp_temp
        return sum(map(sum, dp))



if __name__ == '__main__':
    solution = Solution()
    print(solution.knightProbability_dp(8, 8, 6, 4))