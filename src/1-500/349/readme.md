# 题目
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

# 级别 
Easy

# 算法口号
Use set and intersection.

# 解题思路
Since we don't care about repetitions, we can use set() to get rid of duplicates first. This is O(m+n) time and space.  

Then we can use intersection() to determine the intersection of both sets, which has an average time complexity of O(min(m, n)) with a worst case of O(m*n), and a space complexity of O(m+n).

If we must solve the problem without using any built-in functions, we can always use a Counter to count the appearances of each letter in each list (there's no need to count above 1, actually). Then we output a list containing values where the count is greater than 0 in both Counters. This should be O(m+n) time and space.

Time Complexity: O(m+n) (worst case O(m*n))
Space Complexity: O(m+n)