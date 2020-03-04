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
做法是先找到第一个[0]位大于new Interval[0]的位置，在这个位置插入新值
，然后新建一个结果集合，把第一个值加进去，然后再一个一个加，如果发现有前一个数的结束大于后一个数的起始位的，就取这两个数组最小起始位和最大结束位修改前值。