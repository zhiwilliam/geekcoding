# 154. Find Minimum in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  ***<span style="color:red">[0,1,2,4,5,6,7]</span>*** might become  ***<span style="color:red">[4,5,6,7,0,1,2]</span>***).

Find the minimum element.

The array may contain duplicates.

## Example 1:
```python
Input: [1,3,5]
Output: 1
```
## Example 2:
```python
Input: [2,2,2,0,1]
Output: 0
```

## Note:

* This is a follow up problem to Find Minimum in Rotated Sorted Array.
* Would allow duplicates affect the run-time complexity? How and why?

# Analysis
We can use the binary search algorithm to solve this question. The critical point of this question is to draw a chart to display all the scenarios. The idea is quite similar to Leetcode 33. 