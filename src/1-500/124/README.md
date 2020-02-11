# 题目
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

# 算法口号
深度优先，注意过桥值

# 解题思路
凡是子节点持续和父节点发生关系的基本都用深度优先
这道题的trick在于它有过桥值，就是父节点加左右如果最大也可以成立。那我们就只能使用一个全局的临时变量
maxValue去存储这个最大值。<p>另一个重要的是过桥值一定**不**能是返回值。返回值是本节点加左右儿子最大值或者0
（如果0大于所有的子节点的和， 那就不选子节点，取0值）

# 算法归类
<a href="../../../DSF.md">深度优先搜索</a>