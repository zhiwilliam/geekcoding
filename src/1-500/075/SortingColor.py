from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, current, blue = 0, 0, len(nums)-1
        while current <= blue:
            if nums[current] == 0:
                nums[current], nums[red] = nums[red], nums[current]
                current += 1
                red += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current], nums[blue] = nums[blue], nums[current]
                blue -= 1