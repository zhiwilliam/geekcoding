class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        # counts = collections.Counter(nums)
        nums = sorted(counts)
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([num, num, num])
                else:
                    if -num * 2 in nums:
                        ans.append([num, num, -2 * num])
            if num < 0:
                twoSum = -num
                left = bisect.bisect_left(nums, (twoSum - nums[-1]), i + 1)
                for i in nums[left:bisect.bisect_right(nums, (twoSum // 2), left)]:
                    j = twoSum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])
        return ans
