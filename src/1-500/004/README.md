# 题目
## Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

# 算法口号
二分查找，双指针算index

# 解题思路
这道题一定要画图分析

它的思路就是分别取两个数组的中点，然后比大小。注意这两句很重要<br>
i = (imin + imax) // 2 实现了折半查找<br>
j = half_len - i       这句是在i移动的时候j跟着相对移动。
通过修改imin和imax，它实现了两个数组中同时折半移动。
最后i is perfect的时候的处理分了总长度是奇数个还是偶数个两种情况。

这道题比较复杂，简单几句话很难讲清。建议大家运行几遍体会。不简单。
