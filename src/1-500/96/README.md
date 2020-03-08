题目
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

级别
Medium

解题思路
这道题和95紧密相连，但是我觉得应该两者交换一下位置。
解题办法1: 利用95的code，给出答案的数量，但是performance不够好。
解题办法2: 还是利用recursive function和BST的特性，即left subtree所有node的数值小于root，right subtree所有node的数值大于root。
算法结构：
  首先检查n的值，如果n为0或1，则答案为1
  接下来loop through 1到n的每一个数值：
      每个loop同时recursively计算left subtree和right subtree中的node数量，两者相乘然后计入总数量(因为需要计算不同组合的数量)
解题方法3: 这种算法本质上其实是组合里面的明安图数，所以也可以直接表示为C(2n, n) - C(2n, n - 1)或者(2n)! / ((n+1)!*n!)

Note: 解题办法2因为是recursive所以速度不够快而且大概率有重复计算，所以可以利用functools里面的lru cache来decorate解决办法，这样速度就提升了。
但是解题办法3我写出了两种，一种利用python的math中的factorial算，另一种利用自己写的recursive factorial来计算并且配合lru cache，最终得出自己写的factorial配合cache是最快的方案。

