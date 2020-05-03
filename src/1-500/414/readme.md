# 题目
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

# 级别 
Easy

# 解题思路
The core strategy is similar to finding the maximum number in a list, just with the added requirement of keeping the 3 current maximum values instead of 1.

The solution has a time complexity of O(n) since it traverses the list exactly once, and a space complexity of O(1) since we are only keeping track of a fixed number of values.