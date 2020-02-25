# 177. Nth Highest Salary

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+


# Solution

If you jump into this question in real interview, make sure discuss the definition of Nth highest salary.

Sample Data:

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 120    |
| 3  | 200    |
| 4  | 300    |
| 5  | 300    |
| 6  | 300    |
| 7  | 400    |
+----+--------+

There's no doublt that 1th salary is 400, 2nd salary is 300. 

## But how the 3rd? 

Is it 300? or 200? 

## or, what's the rank for Salary 200? Is it 3rd highest? or 5th?

 
After failed some attemp, now it's clear that as per above sample data, 

The highest salary is 400, 2nd place: 300, 3rd is 200, 4th: 120, and 5th: 100.

The we must use dense_rank to remove duplications of salary.

## Unique result set 

Finally,since dense_rank may result in multiple row with same rank, we need use UNIQUE to keep only one row, otherwise it will threw run time error:

ORA-01422: exact fetch returns more than requested number of rows


