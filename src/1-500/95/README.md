题目
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

级别
Medium

解题思路
这道题比94更加复杂，通过分析题目给出的output得知其要求用preorder traversal来计算。
既然是BST，那么根据BST的特征我们可以得知，对于BST中的任意node，它left subtree的每个node的value一定小于它，它right subtree的每个node的value一定大于它。
(这里默许没有duplicate存在，如果有那么就会增加BST的search时间)
那么我们可以loop through 1到n之间的每个数作为一个root node的值。用一个construct BST的function来建立BST
    假设node为i，那么它的left subtree就是constructBST(head, i - 1)，它的right subtree就是constructBST(i+1, n)
    在第一个nested loop我们固定住left subtree，然后在第二个nested loop里面通过不同的right subtree nodes来构建right subtree，这满足了BST的特征条件，也就是right subtree的root怎么改变都永远大于本node，构建完right subtree之后再跳回上一个loop固定住下一个left subtree的root。。。以此类推

这样我们针对每一个1到n之间的数值i构建一个root：
    然后每个loop更换一次left subtree的root为left：
        然后每个loop更换一次right subtree的root为right：
            root.val = i
            root.left = right
            root.right = right
