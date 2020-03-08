# 题目
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

# 级别 
Easy

# 算法口号
you can't really delete the node.. you just clone the next node and put it in place

# 解题思路
If we don't have the head of a singly-linked list, then we cannot modify the node that points to the input.  
The best we can do is replace the input with a copy of the next node.  

Note: this question is heavily criticized due to the loose wording.