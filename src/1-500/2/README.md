# 题目
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

# 算法口号
非常简单的链表(linked list)问题 + 整除取整

# 解题思路
由于数据是反序存储的, 所以:
1. 我们就像拉拉链一样的一路两两节点数值相加就好.
2. 由于两数相加会大于10, 所以可能要进行进位的考虑, 所以会有另一个"节点"参与拉拉链运动
3. 从第1点到第2点的考量, 我们是用3个节点参与拉拉链.
4. 当一个条链路没有节点时, 另两条链进行拉拉链
5. 当只余下一条链路时, 结束运算.

# 算法归类
<a href="../../../DataStructure.md">线性表-链表</a>
