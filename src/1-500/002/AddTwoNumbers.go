package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var lastNode *ListNode = nil
	var head *ListNode = nil
	last := 0
	for !(l1 == nil && l2 == nil && last == 0) {
		sum_val = last + 0
		if l1 != nil {
			sum_val = sum_val + l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum_val = sum_val + l2.Val
			l2 = l2.Next
		}
		last = sum_val / 10
		sum_val = sum_val % 10
		if lastNode != nil {
			lastNode.Next = &ListNode{sum_val, nil}
			lastNode = lastNode.Next
		} else {
			lastNode = &ListNode{sum_val, nil}
			head = lastNode
		}
	}
	return head
}

func main() {
	fmt.Print(lengthOfLongestSubstring("abcabc"))
}
