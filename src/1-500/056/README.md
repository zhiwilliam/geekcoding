# 题目
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
             
# 级别 
Medium

# 算法口号
排序，持续比较尾数直到发现真正的结尾

# 解题思路
这个题要大胆地使用排序。（注意排序的写法）。用一个start和一个end记录最大化的起始和结尾值。如果发现不连续就加入答案。

# 算法归类
<a href="../../../TE.md">特殊算法</a>
