class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            pre, curr = 0, 0
            for num in nums:
                curr, pre = max(pre+num, curr), curr 
            return curr 
        # since we need calc nums[1:], and nums[:-1],
        # we need consider the exception when only one element in nums
        # which makes both nums[1:] and nums[:-1] are NULL 
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[1:]), helper(nums[:-1]))

