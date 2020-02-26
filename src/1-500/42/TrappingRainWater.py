from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        leftIndex = 0
        rightIndex = len(height) - 1
        water = 0
        while leftIndex <= rightIndex:
            if left <= right:
                if height[leftIndex] > left:
                    left = height[leftIndex]
                else:
                    water += left - height[leftIndex]
                leftIndex += 1
            else:
                if height[rightIndex] > right:
                    right = height[rightIndex]
                else:
                    water += right - height[rightIndex]
                rightIndex -= 1
        return water




solution = Solution()
print(solution.trap([2,0,2]))