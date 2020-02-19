from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len (ratings)
        dp = [1 for _ in ratings]
        for i in range(length - 1):
            if ratings[i + 1] > ratings[i]:
                dp[i + 1] = dp[i] + 1

        for i in range(1, length):
            if ratings[-i] < ratings[-i - 1]:
                dp[-i - 1] = max(dp[-i] + 1, dp[-i - 1])

        return sum(dp)


values = [1,2,87,87,87,2,1]
solution = Solution()
print(solution.candy(values))