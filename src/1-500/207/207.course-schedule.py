#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# Hit: 1) Graph. Represent prerequistites as graph
#      2) Use depth first search + dp to check does it contains cycling.
#
# @lc code=start


from typing import List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dig = {n: {p[1] for p in prerequisites if p[0] == n} for n in range(numCourses)}

        def order(n, dependencies: List[int], path: Set[int]):
            for course_number in dig[n]:
                if course_number in path:
                    return False
                if(course_number not in dependencies):
                    if not order(course_number, dependencies, path | {course_number}):
                        return False
            dependencies.append(n)
            return True

        dependencies = []
        for n in dig:
            if n not in dependencies:
                if not order(n, dependencies, {n}):
                    return False

        return True


if __name__ == '__main__':
    print(Solution().canFinish(8, [
        [2, 4],
        [4, 6],
        [0, 6],
        [0, 7],
        [5, 2],
        [1, 2],
        [3, 2],
        [3, 4]]))

# @lc code=end

