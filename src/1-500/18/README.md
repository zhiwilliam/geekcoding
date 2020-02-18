题目
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

级别
Medium

解题思路
首先找出所有的长度为2的combinations。
将所有combinations中的第二element也就是原list中的element加起来作为新的target，在这个target作为key存入set of dictionaries，combinations中的第一element也就是enumerate出来的index作为value存入刚才dictionary对应的key当中。
loop through这个dictionary的key，找出target - key的complement，如果complement中的value和key的value无共同index，则将key和complement的value中的index作为nums的index找出对应值并且sort，之后加入到结果set当中
