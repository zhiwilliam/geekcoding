class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;

        int[] left = new int[length];
        int[] right = new int[length];
        left[0] = 1;
        right[length - 1] = 1;

        for (int i = 1, j = length - 2; i < length && j >= 0; i++, j--) {
            left[i] = left[i - 1] * nums[i - 1];
            right[j] = right[j + 1] * nums[j + 1];
        }

        int[] arr = new int[length];
        for (int i = 0; i < length; i++) {
            arr[i] = left[i] * right[i];
        }

        return arr;
    }
}