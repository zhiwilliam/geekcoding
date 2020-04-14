
type ListNode struct {
    Val int
 	Next *ListNode
}

func endReached(head *ListNode, n int) bool {
	
	for probe != nil || n > 0 {
		probe = probe.Next
		n--
	}
	return (probe == nil && n == 0)
}
 
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var curr *ListNode = head	
	var probe *ListNode = head
	for curr != nil {
		if endReached(curr,n) {

		} else {
			curr = curr.Next
		}
	}
    
}