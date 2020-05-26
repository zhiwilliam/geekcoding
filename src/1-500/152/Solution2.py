class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax, fmin = [ nums[0]]*2, [nums[0]]*2
        ret = nums[0]
        for index in range(1, len(nums)):
            pre_index = (index - 1)%2
            num = nums[index]
            fmax[index%2] = max( fmax[pre_index] * num, fmin[pre_index]*num, num  )
            fmin[index%2] = min( fmax[pre_index] * num, fmin[pre_index]*num, num  )
            ret = max(max(fmax), ret )
        return ret 

