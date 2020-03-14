class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums: List[int]) -> int:
        # write your code here
        #dp[i]: num for nums[0:i] and nums[i] in the subsequences 
        #dp[i] = max(dp[j])+1 plus 0<=j<i and nums[j] < nums[i]
        
        #dp[0] = 1 
        if not nums:
            return 0
            
        n = len(nums)
        dp = [0]*n 
        
        for i in range(n):
            maxdp = 0 
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                maxdp = max(maxdp, dp[j])
            dp[i] = maxdp + 1                     
        
        return max(dp)

