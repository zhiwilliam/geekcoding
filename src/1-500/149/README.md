https://leetcode-cn.com/problems/max-points-on-a-line/

#  149. 直线上最多的点数

给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
通过次数8,739提交次数42,237


# Solution

Calc the gradiance of two adjuanct points, as well as the point with x=0.

put the two number into dict, add 1 if already exists.

Return the max value of the dictionary.


ATTENTION:
We could not use gradiance directly due to floating round-off error.
Otherwise, it will pass the sample in description, but fail on the following test case:

[[0,0],[94911151,94911150],[94911152,94911151]]

The two points are not line up with (0,0) exactly, but very close.

Instead of, we use two integers denote the slope. The trick is, we need divided them by their GCD, so that we have unique key for same slope. 


