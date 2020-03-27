题目
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

算法归类
Binary search

Appendix by jingdaz:
1. Apply binary search to find 4 mdian elements within merged array. The detailed explanation can be found from link:
https://www.youtube.com/watch?time_continue=1389&v=LPFhl65R7ww&feature=emb_title

2. Java runtime result: 
Runtime: 2 ms, faster than 99.81% of Java online submissions for Median of Two Sorted Arrays.
Memory Usage: 41.9 MB, less than 99.31% of Java online submissions for Median of Two Sorted Arrays.
