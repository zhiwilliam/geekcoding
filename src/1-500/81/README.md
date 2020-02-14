81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

Yes; in worst-case scenario (i.e., all elements in array are identical), BST will not work and sequential search will be conducted which has time complexity O(n).

--------------------------------

Idea:

Compared to Question 33, the tricky part is the array may contain duplicates. There is no better way than advancing just one position when duplicate is encountered as pivot. Search steps:
1. Consider bounary cases
2. Select start point and end point
3. Find the mid point
4. Decide whether mid point falls into non-rotated part or rotated part.
5. Apply normal binary search logic on either non-rotated part or rotated part
6. In case duplicate is encountered, advance start point one spot.


--------------------------------

Runtime: 0 ms, faster than 100.00% of Java online submissions for Search in Rotated Sorted Array II.
Memory Usage: 39.5 MB, less than 52.11% of Java online submissions for Search in Rotated Sorted Array II.

--------------------------------

Runtime: 56 ms, faster than 47.01% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array II.
