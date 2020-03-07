题目
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

级别
Medium

解题思路
这道题下面有问是否能用loop来做，因为recursive的办法实在是太简单了。于是我们利用一个python list来帮助我们走完整个traversal。
base case就是检查是否root为None，这个就不多说了。
接下来在每一个while loop里检查三种情况：
  当前node不为None：将其加入trace list，然后将当前node改为它的left child并且直接进入下一个loop。
  当前node为None，但是trace不为空：说明trace内的这个node有parent node，那么将其pop出trace list，并且加入inorder里面，然后将当前node改为它的right child并且进入下一个loop。
  当前node为None，并且trace为空：说明当前node的parent node为整个tree当中的最后一个node，这是因为它的parent在上一个loop被pop出去之后，我们在当前loop检测到了trace为空说明它的parent的left child亦为None，并且当前node是它parent的right child，也为None，那么它的parent只能是整个tree中的最后一个node。
这里面的关键是选择pop，因为pop不加argument就是pop掉trace的最后一个值，而最后一个值加入到inorder里面顺序就正确了。
