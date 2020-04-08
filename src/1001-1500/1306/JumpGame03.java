class Solution {
    public boolean canReach(int[] arr, int start) {
        
        if(start >= 0 && start < arr.length && arr[start] < arr.length){   
            int val = arr[start];
            arr[start] += arr.length;
            return val == 0 || canReach(arr, start - val) || canReach(arr, start + val);
        }
        return false;
    }
}