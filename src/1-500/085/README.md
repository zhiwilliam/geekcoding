85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

--------------------------------

Idea:

Use Dynamic programming to store partial solution - introduce height for each element where the width of rectangle is calculated by right_boundaries - left_boundaries, therefor area will be production of height and width for each element. After all elements in the two-dimension array have been filled up, do a two loops to find the largest area with all "1"s. The time complexity will be O(N * M, N and M are the dimensions of input integer matrix. 


--------------------------------

Runtime: 5 ms, faster than 79.65% of Java online submissions for Maximal Rectangle.
Memory Usage: 41.7 MB, less than 97.83% of Java online submissions for Maximal Rectangle.

--------------------------------