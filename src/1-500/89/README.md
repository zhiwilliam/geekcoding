# 题目
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

# 算法口号


# 解题思路
这题没有太多的想法，就是一个数学加密，建议死记规律，下面这个是WIKI上找到的规律
From WIKI how binary transfer to GRAY CODE
    #   unsigned int BinaryToGray(unsigned int num)
    #       {
    #           return num ^ (num >> 1);
    #       }

# 算法归类
<a href="../../../DataStructure.md"></a>
