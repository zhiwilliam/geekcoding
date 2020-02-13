# 题目
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.<p>

Example:<p>

Input: [100, 4, 200, 1, 3, 2]<br>
Output: 4<br>
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# 算法口号
HashMap记录，检查，d[i +- left] = length

# 解题思路
这题的解法很巧，我估计当场想不出来

Using a map to save each number's array length. 
Note: The most interesting part is d[i - left] = length and d[i + right] = length.
Very clever, it only update the length value at then end of continuous number. 

# 算法归类
<a href="../../../DataStructure.md">数据结构</a>