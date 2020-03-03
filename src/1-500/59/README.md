# 题目
## Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
             
# 级别 
Medium

# 算法口号
左右往里面挤，注意每次循环完了都要修正

# 解题思路
主要就是玩index，旋转往里面填数字。我坑在了没有在while循环后调整一下x，y。请使用并列的while比较好处理。
