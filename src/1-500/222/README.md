#  222. 完全二叉树的节点个数
https://leetcode-cn.com/problems/count-complete-tree-nodes/

给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

通过次数15,089提交次数22,520

# Solution

## Initial version

If left sub tree and right sub tree has same height h, 
then total node number is 2^h-1 

If not, then recusive process the left sub tree and right sub tree,
one of them must be a Complete Tree, which same time to traval all middle nodes.

Continue process the sub tree which is not Complete.

18 / 18 个通过测试用例
状态：通过
执行用时：92 ms
内存消耗：20.6 MB

执行用时 :92 ms,   在所有 Python3 提交中击败了67.34%的用户
内存消耗 :20.6 MB, 在所有 Python3 提交中击败了21.05%的用户


## Second version

Save the sub tree hight for later use, but seems no obvious improvement.


执行用时 :92 ms,   在所有 Python3 提交中击败了67.34%的用户
内存消耗 :20.6 MB, 在所有 Python3 提交中击败了21.05%的用户

## v3



执行用时 :76 ms,   在所有 Python3 提交中击败了98.46%的用户
内存消耗 :20.6 MB, 在所有 Python3 提交中击败了21.05%的用户
