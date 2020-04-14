package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	} else {
		phantom := &ListNode{0, head}
		var a, b, t, result *ListNode
		for phantom.Next != nil && phantom.Next.Next != nil {
			a, b, t = phantom.Next, phantom.Next.Next, phantom.Next.Next.Next
			b.Next, phantom.Next, a.Next = a, b, t
			phantom = a
			if result == nil {
				result = b
			}
		}
		return result
	}

}
