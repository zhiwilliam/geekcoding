class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # denotes dp[row][col] the minmum path sum for [row][col]
        # then: dp[row][col] = min( dp[row-1][col-1], dp[row-1][col-1]) + triangle[row][col]
        # specific cases for first and last element: 
        #   first element:    dp[row][0] = dp[row-1][0] + triangle[row][0]
        #   last element:     dp[row][row] = dp[row-1][row-1] + triangle[row][row]

        # dp = triangle.copy()
        ct = len(triangle)
        if ct == 1:
            return triangle[0][0]
            
        dp = [ [0]*ct for _ in range(2)]
        dp[0][0] = triangle[0][0]

        for row in range(1,len(triangle)):
            dp_row, dp_pre_row = row%2 , (row-1)%2 

            dp[dp_row][0] = dp[dp_pre_row][0] + triangle[row][0]
            
            for col in range(1, row):
                dp[dp_row][col] = min( dp[dp_pre_row][col-1], dp[dp_pre_row][col]) + triangle[row][col]

            dp[dp_row][row] = dp[dp_pre_row][row-1] + triangle[row][row]
        
        return min( dp[dp_row])
