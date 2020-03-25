#### [114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)

难度**中等**

给定一个二叉树，[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95/8010757)将它展开为链表。

例如，给定二叉树

```
    1
   / \
  2   5
 / \   \
3   4   6
```
将其展开为：
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

### Solution

**(1)先序遍历思路**

这是一个非常容易理解，也容易实现的思路，步骤如下：
- 将右子树接到左子树最右侧叶子结点
- 将左子树接到右边
- 如此往复只到右子树为空

图示 （ 作者：windliang  [原文链接](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/) )

```
    1
   / \
  2   5
 / \   \
3   4   6

//将 1 的左子树插入到右子树的地方
    1
     \
      2         5
     / \         \
    3   4         6        
//将原来的右子树接到左子树的最右边节点
    1
     \
      2          
     / \          
    3   4  
         \
          5
           \
            6
            
 //将 2 的左子树插入到右子树的地方
    1
     \
      2          
       \          
        3       4  
                 \
                  5
                   \
                    6   
        
 //将原来的右子树接到左子树的最右边节点
    1
     \
      2          
       \          
        3      
         \
          4  
           \
            5
             \
              6     

```
时间复杂度：O（N）
空间复杂度：O（1）

代码：

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right 
                continue 

            #find most right leaf for left sub-tree 
            pre = root.left 
            while pre.right: 
                pre = pre.right 
            
            pre.right = root.right 
            root.right = root.left 
            root.left = None 

            root = root.right 
```

执行用时 :48 ms,     在所有  Python3  提交中击败了36.15%的用户
内存消耗 :13.8 MB, 在所有  Python3  提交中击败了5.07%的用户


**(2)后序遍历思路**

TBC


