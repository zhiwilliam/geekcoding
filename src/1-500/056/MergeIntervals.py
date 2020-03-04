from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        if not length: return []
        sorted(intervals, key=lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for it in intervals:
            if it[0] <= end:
                end = max(end, it[1])
            else:
                cur = [start, end]
                res.append(cur)
                start = it[0]
                end = it[1]
        res.append([start, end])
        return res

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
