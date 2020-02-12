class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) 
                 for col_idx, value in enumerate(row) if not value]
        if not zeros:
            return
        rows, cols = map(set, zip(*zeros))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0