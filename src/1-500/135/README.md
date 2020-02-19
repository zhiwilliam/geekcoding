# 题目
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

# 级别 
Hard

# 算法口号
从左往右找递增，从右往左找递增，取最大值。

# 解题思路
这是一个动态规划题，先开一个数组，全部设为1（因为最小值是1），然后从左往右扫描递增的数，找到就在dp数组相应位置加递增的1,<br>
然后再从右往左找递增，找到的话也在相应dp数组位置加递增的1。但此时要取原值和新的值之间最大的那个，防止冲突。

# 算法归类
<a href="../../../DP.md">动态规划</a>