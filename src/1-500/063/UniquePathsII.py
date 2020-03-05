from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        # corner case
        if height == 0 or width == 0: return 0

        # 注意这个开数组
        dp = [[1 for x in obstacleGrid[0]] for y in obstacleGrid]

        print(dp)
        # 第一行
        passable = 1
        for i in range(0, width):
            if obstacleGrid[0][i] == 1:
                passable = 0
            dp[0][i] = passable
        # 第一列
        passable = 1
        for i in range(0, height):
            if obstacleGrid[i][0] == 1:
                passable = 0
            dp[i][0] = passable
        print(dp)
        for y in range(1, height):
            for x in range(1, width):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[height - 1][len(obstacleGrid[0]) - 1]


solution = Solution()
print(solution.uniquePathsWithObstacles([
    [0],[0]
]))