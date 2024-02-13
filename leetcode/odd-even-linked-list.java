/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode oddies = new ListNode();
        ListNode even = new ListNode();
        ListNode newHead = oddies;
        ListNode evenHead = even;
        int count = 1;

        while (head != null){
            if (count  % 2 == 0) {
                even.next = head;
                even = even.next;    
            }
            else {
                oddies.next = head;
                oddies = oddies.next;
            
            }
            count++;
            head = head.next;

        }
        even.next = null;
    oddies.next = evenHead.next;
    return newHead.next;
        
    }
}