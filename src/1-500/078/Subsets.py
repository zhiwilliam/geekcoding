from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, res, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, res, path + [nums[i]])
        res = []
        dfs(nums, 0, res, [])
        return res


solution = Solution()
print(solution.subsets([1, 2, 3]))