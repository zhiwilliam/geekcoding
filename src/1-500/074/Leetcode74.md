# Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

**Example 1:**
```python
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```
**Example 2:**
```python
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```
# Analysis
There is nothing new about this question, it is just a binary search type question. The given matrix is a fully sorted one. We can simply treat this matrix as a sorted "1-dimentional" structure. 
## key points
   1. How to treat the 2D matrix as a linear structure on the fly. This one is quite essential, we need to concatenate the matrix line by line. The length of the sorted 1D structure is the multiplication of row numbers and the column numbers of the matrix
   2. How to map an index of the 1D structure to the index of the matrix.<br>matrix[idx / column numbers][idx % column numbers]

Solved these two key points, the rest task becomes quite simple, try to divide the data structure by half, and recursively search the target in the proper half of the structure. 