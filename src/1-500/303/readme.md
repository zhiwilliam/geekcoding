# 题目
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

# 级别 
Easy

# 算法口号
Build a list that you can re-use

# 解题思路
It looks very straight-forward if you ignored the note that there are **many** calls to the function.  

Since there are many calls, using `sum(nums[i:j+1])` will result in many wasted operations.  

We can do better by building a dictionary to store different combinations we have already seen by using the tuple `(i, j)` as the dictionary key, but it's still too slow.  

We need to leverage the fact that the sum of elements between i and j is also equal to `sum(nums[:j + 1]) - sum(nums[:i])`, and simply build a list of `self.sums = [sum(nums[:i]) for i in range(1, len(nums) + 1)]`. This approach is still not optimal.  

There's in fact an easier way to build this list: since each element in the list is already equal to `sum(nums[:i])`, we only need to add `sums[i]` and `nums[i+1]` to get the list, saving many unnecessary addition operations.  

At last, we pad a 0 to the front of the list so we don't need to check if `i == 1`.