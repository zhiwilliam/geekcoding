# Much slower solution with time complexity of O(n^3)
class Solution:
    def __init__(self):
        self.nums = None
        self.target = None
        self.result_set = []
        self._result_set = self.result_set.append

    def fourSum(self, nums, target):
        self.nums = sorted(nums)
        self.target = target
        self.findList(self.nums, self.target)
        return self.result_set

    def findList(self, nums, target):
        for i in range(len(nums)):
            if i + 1 == range(len(nums)):
                break
            self.threeSum(nums[i], nums[:i] + nums[i+1:], target - nums[i])

    def threeSum(self, fourSumCandidate, nums, target):
        for i in range(len(nums)):
            self.twoSum(fourSumCandidate, nums[i], nums[:i] + nums[i+1:], target - nums[i])

    def twoSum(self, fourSumCandidate, threeSumCandidate, nums, target):
        for i in range(len(nums)):
            if nums == []:
                break
            lastCandidate = target - nums[i]
            if lastCandidate in nums[:i] + nums[i+1:]:
                result = sorted([fourSumCandidate, threeSumCandidate, nums[i], lastCandidate])
                if result not in self.result_set:
                    self._result_set(result)
                    del result


if __name__ == '__main__':
    S = Solution()
    a = [1,0,-1,0,-2,2]
    t = 0
    b = [-479,-472,-469,-461,-456,-420,-412,-403,-391,-377,-362,-361,-340,-336,-336,-323,-315,-301,-288,-272,-271,-246,-244,-227,-226,-225,-210,-194,-190,-187,-183,-176,-167,-143,-140,-123,-120,-74,-60,-40,-39,-37,-34,-33,-29,-26,-23,-18,-17,-11,-9,6,8,20,29,35,45,48,58,65,122,124,127,129,145,164,182,198,199,206,207,217,218,226,267,274,278,278,309,322,323,327,350,361,372,376,387,391,434,449,457,465,488]

    c = 1979
    import time
    start = time.time()
    print(S.fourSum(b, c))
    end = time.time()
    elapsed = end-start
    print('total time is: {}'.format(elapsed))
