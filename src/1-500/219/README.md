https://leetcode-cn.com/problems/contains-duplicate-ii/

# 219. 存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

# Solution

Employed a dictionary ( map in other programing language) to hold all existing 
integer's index in the array. When encounting a new integer, check the previous
index, and comparing with the current index. Return True if they are close enough ( index differs <= k). Otherwise put the interger in dictionary or update the
value of the dictionary for key = current integer.

Trick: Need update the value of the dictionary to the latest index(line# 10),
otherwise it will not satisfy 'absolute difference between i and j is at most k'


# Result

执行结果：通过

显示详情
执行用时 :  40 ms, 在所有 Python3 提交中击败了98.19%的用户
内存消耗 :21.2 MB, 在所有 Python3 提交中击败了27.96%的用户
