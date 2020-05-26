class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax, fmin = nums.copy(), nums.copy()

        for index in range(1, len(nums)):
            num = nums[index]
            pre_index = index - 1 
            fmax[index] = max( fmax[pre_index] * num, fmin[pre_index]*num, num  )
            fmin[index] = min( fmax[pre_index] * num, fmin[pre_index]*num, num  )

        return max(fmax)

