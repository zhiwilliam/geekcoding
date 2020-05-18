# 题目
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

# 级别 
Easy

# 解题思路
This problem is pretty trivial if we are not trying to satisfy the extra requirement "Could you do it without extra space and in O(n) runtime?"

In order to do it without extra space, the trick is understanding that the index of the list is also based on natural numbers. If we traverse the list and use the list's elements as a list of boolean flags to keep track of which number has appeared at least once in the array, then we can use the flags to figure out which numbers hasn't appeared, since that number would be equal to the index of the "flag".

The implementation is to traverse the list, and set the element in position `n` to negative for each number `n` in the list. When we are finished, the positions that don't have a negative value in them correspond to the numbers that haven't appeared.

This solution has `O(n)` time and requires no extra space.