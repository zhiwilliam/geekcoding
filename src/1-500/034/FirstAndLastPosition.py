class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)

        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            first = left
        else:
            first = -1

        if first == -1:
            return [-1, -1]

        last = -1
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                last = mid
                left = mid + 1

        return [first, last]
