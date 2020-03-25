#### [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

难度: **中等**

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树_每个节点_ 的左右两个子树的高度差的绝对值不超过 1。

**示例:**

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树(左）。也可能是[0,-10, 5, null, -3, 9]，如下边右图所示：
``` 
      0                        0
     / \                     /   \
   -3   9                  -10    5 
   /   /                     \     \
 -10  5                      -3     9
```
### Solution

**(1) 转换数组后用Leet108的方法** 

做了上一题108 有序数组转换为BST后，这是最容易想到的办法，**典型的空间换时间思路**

时间复杂度： O(N)，因为每次取中间节点的时间为O(1) 
空间复杂度：O(N) ，因为要开辟同样大小的数组


```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        right, p = 0, head 
        while p:
            right += 1
            nums.append(p.val)
            p = p.next 

        def helper( left, right):
            if left > right:
                return None 
            mid = (left+right)//2 
            node = TreeNode(nums[mid])
            node.left = helper( left, mid-1)
            node.right = helper(mid+1, right)
            return node 

        return helper(0, right-1)
```
执行用时 :80 ms,  在所有  Python3  提交中击败了88.02%的用户
内存消耗 :20 MB, 在所有  Python3  提交中击败了6.10%的用户



**(2) 直接二分法递归** 
重点是找中间的点，由于是链表，需用快慢指针

**Tips** 
- 需要记录慢指针的Prev，因为需要将期next置为NULL，以断开链表
- 但需要注意，当最后**只有两个结点**时，mid == head == pre，此时不能将pre.next设为NULL，因为mid.next需要做右子树的head
- 递归出口：中间节点就是头结点时，表明是最后一个结点了。
- 递归过程中不会有空指针，但最开始需要检测head是否为空

时间复杂度： O(NLogN)，因为每次取中间节点的时间为O(logN) 
空间复杂度：O(LogN)，递归的深度，亦即树的高度，对BST就是LogN 

与上面方法（1）相比，时间复杂度增加了（N -> NlogN)，空间复杂度降低了(N -> LogN)。
```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None 
        
        def findMid(head:ListNode) -> ListNode:
            pre, slow, fast = head, head, head 
            while fast.next and fast.next.next:
                pre, slow, fast = slow, slow.next, fast.next.next 
            if pre != slow:
                pre.next = None 
            return slow 
        
        mid = findMid(head)
        root = TreeNode(mid.val)

        if mid != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root 
```
执行用时 :104 ms,   在所有  Python3  提交中击败了69.31%的用户
内存消耗 :17.1 MB, 在所有  Python3  提交中击败了58.11%的用户

**(3)利用中序遍历思路递归生成BST** 
实际上反着来操作中序遍历

**Tips**
- 递归函数内head需声明为 nolocal 
- 如果递归出口条件为left>=right，则左(left, mid)右（ mid+1, right)，调用（0，len)
- 或者递归出口条件为left>right，左（left, mid-1)，右（mid+1,right)，调用（0，len-1)

时间复杂度： O(N)，每个节点都需要遍历到；	 
空间复杂度：O(LogN) ，平衡二叉搜索树高度上限为LogN。
```python

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None 
        #calc the length of the linked list 
        len, node = 0, head 
        while node:
            len += 1 
            node = node.next 

        def convert( start, end  ):
            nonlocal head 
            if start >= end:
                return None 

            mid = (start + end)//2
            left = convert( start, mid)
            node = TreeNode(head.val)
            node.left = left 

            head = head.next 

            node.right = convert(mid+1, end)
            return node 

        return convert(0, len)
```

执行用时 :72 ms, 在所有  Python3  提交中击败了95.69%的用户
内存消耗 :19.7 MB, 在所有  Python3  提交中击败了6.10%的用户


### 三个方法时间、空间复杂度对比

|项目  |数组 |二分+递归|中序+递归 |
|--|--|--|--|
|时间复杂度| O(N)| O(NlogN)|O(N)|
|空间复杂度|O(N)|O(logN)|O(logN)|



