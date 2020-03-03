# 题目
## Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
             
# 级别 
Hard

# 算法口号
插入，然后从第一个元素开始，再一个一个加进去，合并

# 解题思路
这个题很容易想歪。一开始我分不同情况搞，速度应该可以，但是太复杂。
也不需要用二分查找，因为最后是遍历merge。

