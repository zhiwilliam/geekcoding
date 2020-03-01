/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {

  public ListNode deleteDuplicates(ListNode head) {
    if (head == null) {
      return head;
    }

    ListNode result = new ListNode(0);
    ListNode prev = result;
    prev.next = head;

    ListNode curr = head;

    while (curr != null) {
      while (curr.next != null && curr.next.val == curr.val) {
        curr = curr.next;
      }
      if (prev.next == curr) {
        prev = curr;
      } else {
        prev.next = curr.next;
      }
      curr = curr.next;
    }
    return result.next;
  }
}
