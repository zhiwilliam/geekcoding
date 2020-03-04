# Revised solution
import itertools
import collections
class Solution:
    def __init__(self):
        self.result_set = set()
        self.twoSum = collections.defaultdict(list)

    def fourSum(self, nums, target):
        for (n1, i1), (n2, i2) in itertools.combinations(enumerate(nums), 2):
            self.twoSum[i1+i2].append({n1, n2})
        for t in list(self.twoSum.keys()):
            if not self.twoSum[target-t]:
                continue
            for pair1 in self.twoSum[t]:
                for pair2 in self.twoSum[target-t]:
                    if pair1.isdisjoint(pair2):
                        self.result_set.add(tuple(sorted(nums[i] for i in pair1 | pair2)))
            del self.twoSum[t]
        return [list(r) for r in self.result_set]

if __name__ == '__main__':
    S = Solution()
    a = [1,0,-1,0,-2,2]
    t = 0
    b = [-479,-472,-469,-461,-456,-420,-412,-403,-391,-377,-362,-361,-340,-336,-336,-323,-315,-301,-288,-272,-271,-246,-244,-227,-226,-225,-210,-194,-190,-187,-183,-176,-167,-143,-140,-123,-120,-74,-60,-40,-39,-37,-34,-33,-29,-26,-23,-18,-17,-11,-9,6,8,20,29,35,45,48,58,65,122,124,127,129,145,164,182,198,199,206,207,217,218,226,267,274,278,278,309,322,323,327,350,361,372,376,387,391,434,449,457,465,488]

    c = 1979
    import time
    start = time.time()
    print(S.fourSum(a, t))
    end = time.time()
    elapsed = end-start
    print('total time is: {}'.format(elapsed))