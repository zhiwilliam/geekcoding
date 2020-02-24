# 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

```Python
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
```

# Idea
First, let's research the input matrix. The input matrix is a "***semi-sorted***" structure. In this matrix, data in each row is sorted in ascending from left to right, And data in each column are also in ascending from top to bottom. What we can do is to find a pivot point, and from this pivot point, the other data in the row where the pivot is located is smaller than it, and the other data in its column is larger than it. We can easily find the last value of the first row can be the pivot. 

Second, we can do a comparison zigzaggy. If the target is smaller than the pivot, that means we need to ignore the current column and move to the left because all the data in the current column are bigger than the target. 
Conversely, if the target is bigger than the pivot, that means we must move to the next row because the data in the current row are all smaller than the target. So, we have no chance to find the target in the current row. 

# Source code
```Python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
```