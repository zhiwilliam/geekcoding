public class MaximumSubArray_53 {

    //因为有负数，所以此array一定始于一个正数， 用max记录此正数后面的array sum值得最大值， 直到sum为负数为止，依次循环
    public int maxSubArray(int[] nums){
        int max = Integer.MIN_VALUE, sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum = sum < 0 ? nums[i] : sum + nums[i];
            max = Math.max(max, sum);
        }
        return max;
    }
}
