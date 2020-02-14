
public class Solution86 {

	public ListNode partition(ListNode head, int x) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode left = new ListNode(0);
        ListNode right = new ListNode(0);
        
        ListNode cur = head;
        ListNode curLeft = left;
        ListNode curRight = right;
        
        while (cur != null) {
            if (cur.val < x) {
                curLeft.next = cur;
                curLeft = curLeft.next;
            } else {
                curRight.next = cur;
                curRight = curRight.next;
            }
            cur = cur.next;
        }
            
        curRight.next = null;
       	curLeft.next = right.next;
        
        return left.next;
    }
	
	public static void main(String[] args) {
		Solution86 s = new Solution86();
		
		ListNode a1 = new ListNode(1);
		ListNode a2 = new ListNode(4);
		ListNode a3 = new ListNode(3);
		ListNode a4 = new ListNode(2);
		ListNode a5 = new ListNode(5);
		ListNode a6 = new ListNode(2);
		
		ListNode a = a1;
		a1.next = a2;
		a2.next = a3;
		a3.next = a4;
		a4.next = a5;
		a5.next = a6;
		
		int x = 3;
		ListNode ra = s.partition(a, x);
		System.out.println("partition of " + printListNode(ra) + " becomes " + printListNode(a));
	}
	
	public static String printListNode(ListNode head) {
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		while (head != null) {
			sb.append(head.val + ",");
			head = head.next;
		}
		sb.append("]");
		
		return sb.toString();
	}

}

class ListNode {
    int val;
    ListNode next;
     ListNode(int x) { val = x; }
 }
