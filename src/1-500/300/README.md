#  300. 最长上升子序列

https://leetcode-cn.com/problems/longest-increasing-subsequence/

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

# Solution

## Regular DP, Time Complexity O(n^2)

Denote dp[i] as the lenth of longest increasing subsequence in nums[0:i]

dp[i] = max( dp[j]) + 1 for all j in [0,i) and nums[j]<nums[i] 


## Followp, Time Complexity O(nlogn)

tail[i] denotes the smallest number of the subsequence of lenght i+1 
tail[0] = nums[0]

transition function:
when we iterate to nums[k], we have tail[0:r] 
if we find any j whiich tail[j] > nums[k]
   then we update tail[j] = nums[k]
otherwise we set trail[r] = nums[k]  
 
 
