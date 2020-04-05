from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        buy, hold, max_profit = prices[0], prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < hold:
                max_profit = max(max_profit, hold - buy)
                hold = prices[i]
                if hold < buy:
                    buy = hold
            else:
                hold = prices[i]
        return max(max_profit, hold - buy)


solution = Solution()
print(solution.maxProfit([2,1,2,0,1]))