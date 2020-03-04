from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        appeared = set()
        if len(nums) <= 1:
            return [nums]
        for i in nums:
            if i in appeared:
                continue
            else:
                appeared.add(i)
                nextNums = nums[:]
                nextNums.remove(i)
                for res in self.permuteUnique(nextNums):
                    res.append(i)
                    result.append(res)
        return result


solution = Solution()
print(solution.permuteUnique([1, 1, 2]))