# 题目
## Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

# 级别 
Medium

# 算法口号
深度优先，只把index后面的传入dfs

# 解题思路
很明显的二分查找的题目，是33. Search in Rotated Sorted Array的拓展题目，变的是加了一个可能含有重复数字。

这样的话，如果直接进行左右指针的比较就不知道向哪个方向搜索了，所以，需要在正式比较之前，先移动左指针，是他指向一个和右指针不同的数字上。然后再做33题的查找。

至于查找部分，可以这么考虑：首先nums[l] > num[r]认为是恒成立的。

如果mid指向的位置比nums[l]还大，那么说明l到mid是有序的，这个时候如果nums[l] <= target < nums[mid]说明要查找的在Mid前面，移动右指针；否则要查找的在mid后面，移动左指针。

如果mid指向的位置比nums[r]还小，那么说明mid到r是有序的，然后同样的进行比较操作就行了。

时间复杂度是O(N)，空间复杂度是O(1).