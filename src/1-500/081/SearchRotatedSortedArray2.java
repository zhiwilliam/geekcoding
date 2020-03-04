class Solution {

  public boolean search(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return false;
    }

    int first = 0;
    int last = nums.length - 1;

    while (first <= last) {
      int mid = (first + last) / 2;

      if (nums[mid] == target) {
        return true;
      }

      if (nums[first] < nums[mid]) {
        if (nums[first] <= target && target < nums[mid]) {
          last = mid - 1;
        } else {
          first = mid + 1;
        }
      } else if (nums[first] > nums[mid]) {
        if (nums[mid] < target && target <= nums[last]) {
          first = mid + 1;
        } else {
          last = mid - 1;
        }
      } else {
        first++;
      }
    }

    return false;
  }
}
