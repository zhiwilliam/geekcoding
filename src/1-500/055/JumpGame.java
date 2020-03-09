class Solution {
    public boolean canJump(int[] nums) {
        if (nums == null || nums.length == 0) {
            return true;
        }
        int maxRight = 0;
        for (int i = 0; i < nums.length; i++) {
            if (maxRight < i) {
                return false;
            }
            maxRight = Math.max(i + nums[i], maxRight);
            if (maxRight >= nums.length - 1) {
                return true;
            }
        }
        return false;
    }
}