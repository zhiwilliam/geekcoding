from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[start]:
                if nums[mid] > target and nums[start] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
            if nums[mid] < nums[end]:
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))