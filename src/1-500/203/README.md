#  203. 移除链表元素

删除链表中等于给定值 val 的所有节点。
Remove all elements from a linked list of integers that have value val.
示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-linked-list-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Solution

Iterate all nodes one by one, remove it if matches.

The only trick is to add a dummyNode before head, then all nodes could be processed with same code.

No other tricks. 

