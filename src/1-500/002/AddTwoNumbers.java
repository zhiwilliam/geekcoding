/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum = new ListNode(-1);
        ListNode cur = sum;
        int tens = 0;
        while (l1!= null && l2 != null) {
            int n1 = l1.val;
            int n2 = l2.val;
            
            int n = n1 + n2 + tens;
            if (n >= 10) {
                tens = 1;
                n -= 10;
            }
            else {
                tens = 0;
            }
            
            cur.next = new ListNode(n);
            cur = cur.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        while (l1!= null) {
            int n1 = l1.val;
            int n = n1 + tens;
            if (n >= 10) {
                tens = 1;
                n -= 10;
            }
            else {
                tens = 0;
            }
            
            cur.next = new ListNode(n);
            cur = cur.next;
            l1 = l1.next;
        }
        
        while (l2!= null) {
            int n2 = l2.val;
            int n = n2 + tens;
            if (n >= 10) {
                tens = 1;
                n -= 10;
            }
            else {
                tens = 0;
            }
            
            cur.next = new ListNode(n);
            cur = cur.next;
            l2 = l2.next;
        }
        
        if (tens > 0) {
            cur.next = new ListNode(1);
        }
        
        return sum.next;
    }
}