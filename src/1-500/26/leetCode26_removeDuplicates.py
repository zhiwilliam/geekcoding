class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nextIndex = 1
        preValue = nums[0]
        
        for n in nums[1:]:
            if preValue == n:
                continue
            # new value found 
            nums[nextIndex] = n 
            preValue = n 
            nextIndex +=1 
                
        return nextIndex

