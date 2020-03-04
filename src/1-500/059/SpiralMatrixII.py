from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1 for i in range(n)] for i in range(n)]
        left, right, top, bottom = 0, n, 0, n
        count = 1
        while left < right:
            x, y = left, top
            while x < right:
                matrix[y][x] = count
                count += 1
                x += 1
            y += 1
            x -= 1
            while y < bottom:
                matrix[y][x] = count
                count += 1
                y += 1
            y -= 1
            x -= 1
            while x >= left:
                matrix[y][x] = count
                count += 1
                x -= 1
            x += 1
            y -= 1
            while y > top:
                matrix[y][x] = count
                count += 1
                y -= 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix


solution = Solution()
print(solution.generateMatrix(3))
