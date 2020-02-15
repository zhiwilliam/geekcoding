class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1
        while(low <= high):
            mid = low + int((high - low) / 2)
            mid_value = matrix[int(mid / cols)][int(mid % cols)]
            if mid_value == target:
                return True
            if mid_value > target:
                high = mid - 1
            else:
                low = mid + 1
        return False