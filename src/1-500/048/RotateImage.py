from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = 0
        width = len(matrix[0]) - 1
        h = 0
        height = len(matrix) - 1
        while w <= width:
            for i in range(width - w):
                matrix[h][w + i], matrix[h + i][width], matrix[height][width - i], matrix[height - i][w] = \
                    matrix[height - i][w], matrix[h][w + i], matrix[h + i][width], matrix[height][width - i]
            w += 1
            h += 1
            width -= 1
            height -= 1


matrix = [[2,29,20,26,16,28],
          [12,27,9,25,13,21],
          [32,33,32,2,28,14],
          [13,14,32,27,22,26],
          [33,1,20,7,21,7],
          [4,24,1,6,32,34]]


solution = Solution()
solution.rotate(matrix)
print(matrix)