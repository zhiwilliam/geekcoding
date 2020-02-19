from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, rv = 0, 0
        p = 0
        for i, g in enumerate(gas):
            c = cost[i]
            p += g - c
            if p <= rv:
                rv = p
                res = i
        if p < 0:
            return -1
        return (res + 1) % len(gas)


gas = [3,1,1]
cost = [1,2,2]
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

solution = Solution()
print(solution.canCompleteCircuit(gas, cost))