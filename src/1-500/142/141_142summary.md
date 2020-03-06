# Leetcode 问题141和142 心得总结
by [Jiarui Yang] (www.linkedin.com/in/jiarui-jordan-yang-45451811b)

----
## 问题
[问题141](https://en.wikipedia.org/wiki/Markdown)
[问题142](https://leetcode.com/problems/linked-list-cycle-ii/)

> 141: Find if there is a cycle in a LinkedList.

> 142: Find if there is a cycle in a LinkedList. If there is a one, return starting node of the cycle.

----
## Compiler
1. Python 3

----
## 土豪任性法(brute force)
**前提有无限的memory及时间**

* a pointer to the starting point of LinkedList & list
* The pointer loop the LinkedList, for each node, check if the node is already in the list. If node is already in the list, return True(141) or the node(142). 
* Time complexity O(n^2) 

>pseudocode

    list = [] 
    current = head
    while current.next != None:
       if current in list:
            return True/head.
       else:
          list.append(current)
          current = current.next


----
## 龟兔赛跑法
** 目前最优法 **

* two pointers, points to the starting node of the LinkedList 
* First pointer(turtle, normal speed), second pointer(hare, twice speed as the turtle)
* If hare and turtle points at the same node, return True(141), if hare.next == None, it means the hare pointer reaches the end of the LinkedList, return False. (141)  
* If there is a cycle. Change Hare to point to the starting point of the LinkedList at the same speed as the turtle pointer.
* The starting node of the cycle should be the node where hare and turtle match again. 

>142 solutions with comments

    class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #龟兔赛跑问题
        #解题思路：龟node一次走一步，兔node一次走两步，如果龟兔撞上了，return true，else false

        #situation 1: empty linkedlist
        if head == None:
            return None
        dummy = ListNode(None) #dummy node
        dummy.next = head
        
        #initalize 
        tortoise = dummy
        hare = dummy
        
        while True:
            #situation 2: no cycle
            if(hare.next == None or tortoise.next == None):
                return None
            
            tortoise = tortoise.next
            hare = hare.next.next
            
            # situation 3: if hare jump too fast...
            if(hare == None):
                return None
            # situation 4: match, exit the loop, starting to find the node.
            if(tortoise == hare):
                break
        # reset the hare pointer to the starting node        
        hare = dummy 
        while True:
            #change the speed of hare
            tortoise = tortoise.next
            hare = hare.next
            
            if(tortoise == hare):
                return hare
            
            
        return None


----
## 龟兔赛跑算法其他用法
* [检测是否有一个int list有无重复数字](https://www.youtube.com/watch?v=pKO9UjSeLew)
