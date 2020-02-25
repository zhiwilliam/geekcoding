from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])




solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))