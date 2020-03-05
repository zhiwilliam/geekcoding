from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        dp = [100000 for i in grid[0]]
        for y, list in enumerate(grid):
            for x, value in enumerate(list):
                if x == 0:
                    if y == 0:
                        dp[x] = grid[y][x]
                    else:
                        dp[x] = dp[x] + grid[y][x]
                else:
                    dp[x] = min(dp[x] + grid[y][x], dp[x - 1] + grid[y][x])

        return dp[-1]



solution = Solution()
print(solution.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
