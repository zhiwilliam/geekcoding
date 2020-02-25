# 题目
First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

# 级别 
Hard

# 算法口号
while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]: 交换值

# 解题思路
这道题其实是用时间换空间, 我不知道它为啥也算成O(n)。它其实是不断地把外面的值换到你应该插入的那个位置, 直到找到对的那个值。

# 算法归类
<a href="../../../TE.md">特殊题</a>