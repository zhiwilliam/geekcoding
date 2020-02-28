# Problem 

编写一个 SQL 查询，查找所有至少连续出现三次的数字。

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/consecutive-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Solution

Employed Oracle Analytic function to proceed only 3 rows prior current row.

First version use AVG which failed for the first row always satisfy the filter 
condition of : num = v 

Use SUM to avoid this edge case. But it may fail with following test case:
Num  Sum
 1     1 
 3     4
 2     6 

So added Min function to handle it.

Since Sum() = 3*num and min = num, we can guarentee that all three numbers 
are equal to num.



