# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start, end = head, head.next
        while end:
            print(start.val, end.val)
            if start.val != end.val:
                start.next = end
                start = end
            end = end.next
        start.next = end
        return head


        