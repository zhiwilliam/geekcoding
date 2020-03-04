class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        nums_len = len(nums)

        left = -1

        for i in range(nums_len - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            left = i
            break

        if left == -1:
            nums[:] = nums[::-1]
            return
        if left == nums_len - 2:
            nums[-2], nums[-1] = nums[-1], nums[-2]
            return

        right = self.B_search(nums, left + 1, nums_len - 1)
        nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1:] = nums[left + 1:][::-1]
        return

    def B_search(self, nums, left, right):
        target = nums[left - 1]
        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                right = mid - 1
            else:
                left = mid

        if nums[right] > target:
            return right
        return left
