# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if count >= n:
                slow = slow.next
            count += 1
            fast = fast.next 
        if slow.next:
            slow.next = slow.next.next
        return dummy.next
        
        
            
        
        