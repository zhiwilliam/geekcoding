public class Solution {
    public int searchInsert(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        int mid;
        
        if(target < nums[0]) return 0;
        
        while(lo + 1 < hi){
            mid = lo + (hi - lo)/2;
            if(target == nums[mid]){
                return mid;
            }
            else if(target < nums[mid]){
                hi = mid;
            }
            else{
                lo = mid;
            }
            
        }
        
        if(target == nums[hi]) return hi;
        if(target > nums[hi]) return hi + 1;
        if(target == nums[lo]) return lo;
        return lo + 1;
    }
}
