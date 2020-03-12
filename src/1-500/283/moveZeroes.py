class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

    def moveZeroes_1(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1