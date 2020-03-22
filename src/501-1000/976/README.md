# 题目
## Largest Perimeter Triangle
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6



# 级别 
Easy

# 解题思路

For a >= b >= c, a,b,c can form a triangle if a < b + c.
1. sort the list A
2. try to get a triangel with the largest 3 numbers.
3. if A[i]<A[i-1]+A[i-2] then we get a triangel
else cannot get it.
4.repeat step2 and step3 with the left numbers.




# 算法归类
Math

