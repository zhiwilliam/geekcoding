class Solution:
    def rob(self, nums: List[int]) -> int:
        
        pre, curr = 0, 0 
        for num in nums:
            curr, pre = max( pre + num, curr), curr 

        return curr

