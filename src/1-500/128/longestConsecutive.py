import collections
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        ans = 0
        for i in nums:
            if i not in d:              # i is number from dictionary
                left = d.get(i - 1, 0)  # 0 is default value if not found
                right = d.get(i + 1, 0)
                length = left + right + 1
                ans = max(ans, length)

                d[i] = length
                d[i - left] = length
                d[i + right] = length

        return ans


solution = Solution()
print(solution.longestConsecutive([1, 3]))
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([50, 1, 200, 3, 4, 2]))
