# 题目
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

# 级别 
Easy

# 算法口号
Two pointers solves an array of array problems

# 解题思路
The problem states "in-place" and "minimize operations", which can be interpreted a few ways depending on whether another array can be used and whether swapping a pair of array elements counts as one operation.  

Since we are under scrutiny, let's assume the interviewer operates under old-school, draconian rules: no additional memory can be used except a buffer to swap elements, and a swap is considered three separate operations (temp = a; a = b; b = temp;).

A potential optimal solution can be designed using two pointers. The idea is traversing the array and writing each non-zero element to the beginning, following the previous non-zeros, then writing zero to the rest of the array. The fast pointer will start at 0 and traverse the array, while the slow pointer will start at 0 and keep track of where a non-zero element should be inserted. This guarantees n reads and n writes, with O(1) space just for the pointers.

Another potentially optimal solution, when the array contains more than 2/3 zeroes, is a variation of the previous design, where we swap a zero with a non-zero whenever we see one. In this case, we use the slow pointer to keep track of the position of the left-most zero in the array, and the fast pointer to traverse the array. When the fast-pointer finds a non-zero, it gets swapped with the left-most zero.