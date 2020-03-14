class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tail[i] denotes the smallest number of the subsequence of lenght i+1 
        # tail[0] = nums[0]

        # transition function:
        # when we iterate to nums[k], we have tail[0:r] 
        # if we find any j whiich tail[j] > nums[k]
        #    then we update tail[j] = nums[k]
        # otherwise we set trail[r] = nums[k]  

        if not nums: return 0 

        n = len(nums)

        tail = []  
        for num in nums:
            if not tail or num > tail[-1]:
                tail.append(num)
                continue 
            # bi search tail to find the first tail[j]>num 
            left, right = 0, len(tail)-1 
            loc = right 
            while left <= right:
                mid = (left+right)//2
                if tail[mid] >= num: ## must use >=, otherwise failed on:[4,10,4,3,8,9]
                    loc = mid 
                    right = mid - 1
                else:
                    left = mid + 1 
            tail[loc] = num 

        return len(tail)

