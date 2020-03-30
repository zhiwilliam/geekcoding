class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #dp, denotes dp[row][col] = dp[row-1][col-1] + dp[row-1][col] for col >= 1, row >= 1 
        #dp, dp[row][0] = 1 , dp[row][row] = 1
        dp = [ [1] * (rowIndex+1) for _ in range(2)]

        for i in range(1,rowIndex+1):
            for j in range(1, i ): 
                dp[i%2][j] = dp[(i -1)%2][j-1] + dp[(i-1)%2][j]

        return dp[i%2]
