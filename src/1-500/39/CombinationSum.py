class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        self.findComb(candidates, 0, target, [], result)
        return result

    def findComb(self, candidates, index, target, curr, result):
        if target == 0:
            result.append(list(curr))
            return

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            curr.append(candidates[i])
            self.findComb(candidates, i, target - candidates[i], curr, result)
            curr.pop()