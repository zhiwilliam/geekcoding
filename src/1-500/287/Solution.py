class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = nums[0], nums[nums[0]] 
        while slow  != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        find = 0
        while find != slow:
            find = nums[find]
            slow = nums[slow]
        
        return find 

