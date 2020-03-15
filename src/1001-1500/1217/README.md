# 题目
## Play with Chips

There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

Move the i-th chip by 2 units to the left or to the right with a cost of 0.
Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.

Return the minimum cost needed to move all the chips to the same position (any position).

 

Example 1:

Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
Example 2:

Input: chips = [2,2,2,3,3]
Output: 2
Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
 

Constraints:

1 <= chips.length <= 100
1 <= chips[i] <= 10^9



# 级别 
Easy


# 解题思路
We can move a chip at any position to 2 positions left or 2 positions right at no cost at all. 
So we can keep moving all chips at positions of even numbers to position 2 at no cost,
and all chips at odd positions to position 1 at no cost. 
Now, we have x chips at position 1 and y chips at position 2.
If x > y, then move all y chips by 1 unit to the right to be at position 2, and return y. 
But if y > x, then move all x chips by 1 unit to the left to be at position 1, and return x.

Essentially, we're counting how many odd numbers and even numbers there are and returning the smaller count.
chips = [1,2,3]. 2 odd numbers and 1 even number. Return 1.
chips = [2,2,2,3,3]. 2 odd numbers and 3 even numbers. Return 2.
chips = [1,3,5,7,9,11,2,4]. 6 odd numbers and 2 even numbers. Return 2.

# 算法归类
Math
