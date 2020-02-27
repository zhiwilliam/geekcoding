#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# Reference to 207
#
# @lc code=start

from typing import List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dig = {n: {p[1] for p in prerequisites if p[0] == n} for n in range(numCourses)}

        def order(n, dependencies: List[int], path: Set[int]):
            for course_number in dig[n]:
                if course_number in path:
                    return False, dependencies
                if(course_number not in dependencies):
                    (c, dependencies) = order(course_number, dependencies, path | {course_number})
                    if not c:
                        return False, dependencies
            dependencies.append(n)
            return True, dependencies

        dependencies = []
        for n in dig:
            if n not in dependencies:
                (c, dependencies) = order(n, dependencies, {n})
                if not c:
                    return []

        return dependencies


if __name__ == '__main__':
    print(Solution().findOrder(4, [[1, 0], [2, 0], [0, 3]]))

# @lc code=end

