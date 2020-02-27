from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) <= 1:
            return [nums]
        for i in nums:
            nextNums = nums[:]
            nextNums.remove(i)
            for res in self.permute(nextNums):
                res.append(i)
                result.append(res)
        return result


solution = Solution()
print(solution.permute([]))