from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        result = reach = maxReach = 0
        for index, num in enumerate(nums):
            if index > reach:
                reach = maxReach
                result += 1
            maxReach = max(maxReach, index + num)
        return result


solution = Solution()
print(solution.jump([0]))
print(solution.jump([2,3,1,1,4]))