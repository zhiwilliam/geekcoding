# Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

## Example 1:

```python
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

## Example 2:
```python
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```
# Analysis
I think this is the easiest medium difficualt question on Leetcode. To solve this question, the train of thought is very intruitive, targeting the rows and the columns which should be set to 0 and set them. 

I have two solutions for this question. The first one is the intruitive solution which jumps to my mind at the fist time when I saw this question. This solution is not the most efficient one, but it is very easy to understand. And the second solution is the space effective one.
## 1. Intruitive solution
In this solution, I need to scan the matrix two times. The rows and collumns which should be set to 0 are found in the first scan. I use two sets to store the row numbers and the collumn numbers. Once we locate the rows and the columns which should be 0, we can start the second scan and set the rows and columns which is in the row or column sets to 0 in place.
### The first scan
```python
zeros = [(row_idx, col_idx) 
        for row_idx, row in enumerate(matrix) 
        for col_idx, value in enumerate(row) if not value]
```
The first scan returns a list of tuples. Each tuple item contains the row and column index of a 0 element in the matrix. 

For example, if the matrix is:
``` python
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
```
Then the return value of the first scan is:
```python
[(0, 0), (0, 3)]
```
There is an edge case, there is not 0-element in the original matrix. In this scenario, we don't have to do anything but return. 

After getting this list of tuples, we can make the sets for the rows and columns which should be set to 0.
```python
if not zeros:
    return
rows, cols = map(set, zip(*zeros))
```
### The second scan
```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i in rows or j in cols:
            matrix[i][j] = 0
```

### *Time Complexity and Space Complexity analysis
1. TC
   <br>We go through the matrix 2 laps. Then the TC is: <span style="color:pink">***O(mn)***</span>
2. SC
   <br>In the first scan, I used a List Comprehension. And the worst case is the matrix is an all 0 matrix. So, the space complexity is <span style="color:pink">***O(mn)***</span>