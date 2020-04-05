# 题目
## Largest Rectangle in Histogram
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

# 级别 
Hard

# 算法口号

# 解题思路
这个题是单调栈的运用，使用一个单调递增栈来维护已经出现了的矩形高度，如果后面新来的元素高度比栈里最后的元素高，那么需要入栈，因为面积最大的元素会出现在后面。如果后面新来的元素高度比栈里的最后的元素小，那么需要弹出栈里的元素，并且，每次弹出的时候都要对计算目前的宽度，相乘得到面积。

栈里保存索引的方式是需要掌握的，保存索引的方式在最小值栈结构中也有运用。

每次求栈内矩形的高度的时候，其实是求其位置到最右边的距离。注意即将入栈的元素索引i是一直不变的，另外栈里的每个元素的索引可以认为是矩形的右边界。

这个题余姚先Pop，再计算宽度，如果不这么搞的话，对于[6,5]这样的测试用例，会求出最大面积是6，而不是10.

Leetcode #84 Largest Rectangle in Histogram图文并茂，讲得很清楚。

最坏时间复杂度是O(N^2)，最优时间复杂度是O(N)，空间复杂度是O(N)。