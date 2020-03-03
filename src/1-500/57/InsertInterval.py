from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        i = 0  # Find the right location, insert a new interval, regardless of the overlap problem
        while i < len(intervals):
            if intervals[i][0] > newInterval[0]:
                break
            i += 1

        intervals.insert(i, newInterval)  # Insert new interval

        res = [intervals[0]]  # Define the result list and put the first element in it

        for i, e in enumerate(intervals, 1):  # Add new elements in turn, and consider overlapping issues
            if e[0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], e[-1])
            else:
                res.append(e)
        return res


solution = Solution()
#print(solution.insert([[4, 5]], [1, 6]))
#print(solution.insert([[4, 5]], [1, 2]))
# print(solution.insert([[4, 8]], [5, 6]))
# print(solution.insert([[4, 8]], [5, 9]))
# print(solution.insert([[4, 8]], [9, 19]))
print(solution.insert([[1, 3], [4, 8], [9, 10]], [3, 5]))
#print(solution.insert([[1, 5], [8, 9], [11, 12], [14, 15]], [6, 13]))