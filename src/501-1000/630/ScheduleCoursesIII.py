from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        que = []
        cur = 0
        for t, d in courses:
            heapq.heappush(que, -t)
            cur += t
            if cur > d:
                cur += heapq.heappop(que)
        return len(que)