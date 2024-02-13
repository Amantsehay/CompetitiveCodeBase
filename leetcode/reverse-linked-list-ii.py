# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        count = 1
        lastHead = None
        firstLast = None
        nextHead = None
        curr = head
        prev = None
        while count < left:
            firstLast = curr
            curr = curr.next
            count += 1
        lastHead = curr
        while count <= right:
            nextHead = curr.next
            curr.next = prev
            prev = curr
            curr = nextHead
            count += 1
        if firstLast:
            firstLast.next = prev
        else:
            head = prev
        lastHead.next = curr
        return head
        