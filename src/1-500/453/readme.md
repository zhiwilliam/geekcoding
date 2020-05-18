# 题目
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

# 级别 
Easy

# 解题思路
We arrive at the solution by observing a few facts first:
1. Incrementing `n-1` elements is the same as decrementing `1` element if all we care about is making the equality between the numbers
2. Based on #1, we can compute the number of moves needed by subtracting the minimum value from all list elements, then returning the sum the elements. Since we can only reduce 1 element by 1 during each move, this should give us the total number of moves required to reduce all elements to zero.

With those observations, it isn't hard to compute the number of moves directly.