class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums is None or len(nums) == 0:
            return False
        first, last = 0, len(nums) - 1

        while first <= last:
            mid = (first + last) // 2

            if nums[mid] == target:
                return True

            if nums[first] < nums[mid]:
                if nums[first] <= target and target < nums[mid]:
                    last = mid - 1

                else:
                    first = mid + 1

            elif nums[first] > nums[mid]:
                if nums[mid] < target and target <= nums[last]:
                    first = mid + 1

                else:
                    last = mid - 1

            else:
                first += 1

        return False