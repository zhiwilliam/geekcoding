
# 题目
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

# 级别
Medium

# 解题思路
我们在这里总结一下两种可能的思路（只考虑被除数和除数均为正数的情况）：

1、只要被除数大于等于除数，就从被除数中减去除数，每减去一次结果就增加1。假设最终结果为n，则该算法的时间复杂度为O(n)。

2、只要被除数大于等于除数的2倍，我们就将除数和结果均乘以2，直到被除数小于除数的2倍。接着将被除数更新为被除数与除数的差，将除数恢复为最初的除数，并重复上述操作直到被除数小于除数。此时算法的时间复杂度降为O(logn）。

       O(logn)的复杂度要比O(n)好不少的。而这刚好涉及到几何级数和代数级数的概念。因为思路1中被除数是以代数级数的速度下降的，所以其时间复杂度为O(n)；而思路2中除数是以几何级数的速度增长的，所以迭代中被除数也就是以几何级数的速度下降的，因此其时间复杂度为O(logn）。

       注意上述分析中n并不表示被除数和除数的规模，而是代表结果的规模。这类问题我们一般称为output-sensitive的。

       好多问题都可以从O(n)优化为O(logn)，而这也是面试中经常会碰到的问题。我记得中Leetcode中还有好几道题目涉及到这一思想，例如求平方根，求幂等。建议读者把这几道题目结合起来一起练习，加深印象。

最后的针对-2147483648和2147483647作为dividend的结果判定。

