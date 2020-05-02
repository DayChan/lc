package yc.ma.leetcode;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
}
public class j2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int ad1 = l1.val;
        int ad2 = l2.val;
        ListNode solution = new ListNode((ad1 + ad2) % 10);
        solution.next = null;
        int carry = (ad1 + ad2) / 10;
        ListNode p = solution;
        while (l1.next != null || l2.next != null || carry != 0) {
            if (l1.next != null) {
                l1 = l1.next;
                ad1 = l1.val;
            }
            else {
                ad1 = 0;
            }
            if (l2.next != null) {
                l2 = l2.next;
                ad2 = l2.val;
            }
            else {
                ad2 = 0;
            }
            p.next = new ListNode((ad1 + ad2 + carry) % 10);
            p = p.next;
            p.next = null;
            carry = (ad1 + ad2 + carry) / 10;
        }
        return solution;
    }
}
