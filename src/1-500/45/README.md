# 题目
## Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

# 级别 
Hard

# 算法口号
贪心算法

# 解题思路
哎，我估计贪心算法大家真的是需要仔细看一下的。一开始挺难理解。
第一步没啥好选的，就是从第一个index取它的值往后跳。
然后遍历下一个点加下一个点的值，看看它最远可以跳到哪里？然后第二跳就跳到这个最远的点。
以此类推。

# 算法归类
<a href="../../../Greedy.md">贪心算法</a>