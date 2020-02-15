# 题目
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

# 算法口号


# 解题思路
传统的Java Merge two array, 好处就是题目的两个array已经是sorted的了就可以直接对比就好。注意题目要求不要返还值，所以结束的时候
要把new array 赋值到原list上

# 算法归类
<a href="../../../DataStructure.md"></a>
