# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        midd = self.getMid(head)
        last = self.reverse(midd)
        curr = head
        while curr and last:
            print(last.val, curr.val)
            if curr.val != last.val:
                return False
            curr = curr.next
            last = last.next
        return True

    def getMid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self, head):

        prev, curr = None, head
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
        