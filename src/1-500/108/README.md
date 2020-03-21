### [108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

难度:简单

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树_每个节点_ 的左右两个子树的高度差的绝对值不超过 1。

**示例:**

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
```
          0
         / \
       -3   9
       /   /
     -10  5
```

###  Solution

Keyword： **递归**

思路： 取数组中间的数为根，分别对左/右进行递归调用


代码：

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # choose nums[n//2] as root, then recursive  left and right 
        ct = len(nums) 
        if ct == 0:
            return None 

        mid = ct //2 
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:]) #注意要 +1 

        return root 
```

执行用时 :60 ms,   在所有  Python3  提交中击败了83.03%的用户
内存消耗 :15.8 MB, 在所有  Python3  提交中击败了 5.25%的用户

