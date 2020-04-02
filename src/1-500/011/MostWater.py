from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                l -= 1
        return ans


solution = Solution()
print(solution.maxArea([1,2,4,3]))