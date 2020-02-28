#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# 1) Two pointers: Iterate first pointer(p1) alonge with Iterating the second pointer(p2) fron p1 to indicate subset of the array. compare the length of 
#    subset from p1 to p2 with previous result, update result by the shorter one until p1 reach the end of dataset.
#
# @lc code=start

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        r = 0
        p2 = 0
        e = 0
        for p1 in range(0, len(nums)):
            (_r, p2, e) = self.check(s, nums, p1, p2, e, r)
            if r == 0 or (_r != 0 and _r < r):
                r = _r
            e -= nums[p1]
        return r

    def check(self, s: int, nums: List[int], p1: int, p2: int, e: int, r) -> int:
        _r: int = 0
        if e < s:
            for _p2 in range((len(nums)-1 if len(nums)-1 < p2 else p2), len(nums)):
                _r = 1 + (_p2-p1)
                if p2 <= (len(nums)-1):
                    e += nums[_p2]
                if e >= s:
                    return _r, _p2+1, e
            return 0, _p2+1, e
        else:
            return p2-p1, p2, e


if __name__ == '__main__':
    print(Solution().minSubArrayLen(15, [1,2,3,4,5]))

# @lc code=end

