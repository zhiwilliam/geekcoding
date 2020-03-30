class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # denotes dp[row][col] the minmum path sum for [row][col]
        # then: dp[row][col] = min( dp[row-1][col-1], dp[row-1][col-1]) + triangle[row][col]
        # specific cases for first and last element: 
        #   first element:    dp[row][0] = dp[row-1][0] + triangle[row][0]
        #   last element:     dp[row][row] = dp[row-1][row-1] + triangle[row][row]
        dp = triangle.copy()

        for row in range(1,len(triangle)):
            dp[row][0] = dp[row-1][0] + triangle[row][0]
            for col in range(1, row):
                dp[row][col] = min( dp[row-1][col-1], dp[row-1][col]) + triangle[row][col]

            dp[row][row] = dp[row-1][row-1] + triangle[row][row]
        
        return min( triangle[-1])      
