from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        numlen = len(nums)
        l, r = 0, numlen - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


solution = Solution()
print(solution.search([2,5,6,0,0,1,2], 3))