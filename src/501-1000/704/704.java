class Solution {
    public int search(int[] nums, int target) {
        if(nums == null || nums.length == 0) return -1;
        if(target < nums[0] || target > nums[nums.length -1]) return -1;
        
        int lo = 0, hi = nums.length - 1;
        while (lo + 1 < hi){
           int mid = lo + (hi - lo)/2;
            if (target == nums[mid]){
                return mid;
            } else if (target < nums[mid]){
                hi = mid;
            } else {
                lo = mid;
            }
        }
        
        if (nums[hi] == target) return hi;
        if (nums[lo] == target) return lo;
        return -1;
    }
}
