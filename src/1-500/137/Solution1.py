class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        elements = set(nums)
        
        return (3*sum(elements) - sum(nums) )//2

