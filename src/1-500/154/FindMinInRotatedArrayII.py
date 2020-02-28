from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
                left += 1
            else:
                right -= 1
        return nums[left]