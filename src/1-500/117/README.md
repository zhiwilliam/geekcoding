#### [117. 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

难度**中等**

给定一个二叉树
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为  `NULL`。

初始状态下，所有 next 指针都被设置为  `NULL`。

**进阶：**

-   你只能使用常量级额外空间。
-   使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

**示例：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)

**输入**：root = [1,2,3,4,5,null,7]
**输出：**[1,#,2,3,#,4,5,7,#]
**解释：**给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

**提示：**

-   树中的节点数小于  `6000`
-   `-100 <= node.val <= 100`

### Solution
与上一题（116）相比，唯一的区别是取消了**完全树**的条件，故需要考虑以下不同的情况：
- 只有左子树
- 只有右子树
- 没有子树

**(1)BSF**
由于BSF方法并不要求是完全树，故上题的做法可以原封不动地直接用在这里。
```python
from collections import deque 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque([root])
        while q:
            pre = None 
            for _ in range(len(q)):
                node = q.popleft()
                if pre:
                    pre.next = node 
                pre = node 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root 
```
- 执行用时 :56 ms, 在所有  Python3  提交中击败了75.64%的用户
- 内存消耗 :14.8 MB, 在所有  Python3  提交中击败了5.94%的用户

**(2)递归**
原题解链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/di-gui-fa-jian-dan-yi-dong-ban-xin-shou-kan-by-lov/
作者：lovXin

思路是对每一个树的根结点，对其左右子树递归调用时，针对不同的情况，采取不同的连接:
- 左子右子都有，则左子next指向右子，右子next指向getNextNoNullChild
- 只有左子，左子next指向getNextNoNullChild，
- 只有右子，右子next指向getNextNoNullChild，

其中getNextNoNullChild是关键，是根据当前root，向右找到第一个有下一级的结点（左，右，或左右者都有），并优先返回这个下一级的左节点。

**Tips**

递归时要先递归右子树，否则上级节点next关系没建好，下级无法成功getNextNoNullChild

作者提供的Java版，Python实现如下：

```python

class Solution:
    def findNextChild(self,root):
        while root.next:
            root = root.next 
            if root.left:
                return root.left 
            if root.right:
                return root.right 
        return None 


    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        if not root or ( not root.left and not root.right):
            return root 

        if root.left and root.right:
            root.left.next = root.right 
            root.right.next = self.findNextChild(root)

        if not root.left:
            root.right.next = self.findNextChild(root)

        if not root.right:
            root.left.next = self.findNextChild(root)

        self.connect(root.right)
        self.connect(root.left)
        
        return root         
```

- 执行用时 :  92 ms, 在所有  Python3  提交中击败了11.12%的用户
- 内存消耗 :14.8 MB, 在所有  Python3  提交中击败了 5.94%的用户

