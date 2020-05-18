class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # nums = [x - min(nums) for x in nums]
        # counter = 0
        # while (sum(nums) > 0):
        #     nums[nums.index(max(nums))] -= 1
        #     counter += 1
        # return counter
        
        
        # better way of doing the above
        return sum(nums) - len(nums) * min(nums)