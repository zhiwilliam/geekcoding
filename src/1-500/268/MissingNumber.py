from typing import List

class Solution:
    def missingNumber_brute_force(self, nums: List[int]) -> int:
        # This is not duplication in nums, to accelerate the search, we use set.
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i    
        return -1
    
    def missingNumber_bit(self, nums: List[int]) -> int:
        res =  len(nums)
        for idx, value in enumerate(nums):
            res ^= idx ^ value
        return res

    def missingNumber_gauss_formula(self, nums: List[int]) -> int:
        n = len(nums) + 1
        return n*(n-1)//2 - sum(nums)