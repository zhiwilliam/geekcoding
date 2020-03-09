class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return 0;
        }
        int jump = 0;
        int curEnd = 0;
        int furthest = 0;
        for (int i = 0; i < nums.length; i++) {
            furthest = Math.max(furthest, i + nums[i]);
            if (curEnd == i) {
                jump++;
                curEnd = furthest;
            }
            if (curEnd >= nums.length - 1) {
                return jump;
            }
        }
        return jump;
    }
}