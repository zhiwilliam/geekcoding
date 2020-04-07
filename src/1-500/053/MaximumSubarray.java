class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        
        int length = nums.length;
        int[] dp = new int[length];
        dp[0] = nums[0];
        int max = dp[0];
        
        for(int i = 1; i < length; i++){
            
            dp[i] = (dp[i-1] < 0) ? nums[i] : dp[i-1] + nums[i];
            max = Math.max(dp[i], max);
        }
        
        return max;
        
    }
}