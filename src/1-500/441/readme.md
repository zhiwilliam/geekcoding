# 题目
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

# 级别 
Easy

# 解题思路
It's a straight forward solution if we use a loop, but the fastest solution uses the fact that for a arithmetic series that increments by 1 between each element, `sum = (x + 1) * x / 2`. By solving this equation for x and ignoring the negative value, we get `x = (-1 + sqrt(8 * n + 1)) / 2`. We can simply substitute n into the equation and get the value of x after flooring the result so we arrive at an integer value.