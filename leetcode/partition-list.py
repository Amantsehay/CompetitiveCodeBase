# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        lessNodes = Node()
        greaterNodes = Node()
        newHead = lessNodes
        great = greaterNodes
        curr = head
        while curr:
            if curr.val < x:
                lessNodes.next = curr
                lessNodes = lessNodes.next

            else:
                greaterNodes.next = curr
                greaterNodes = greaterNodes.next
            curr = curr.next
        greaterNodes.next = None
        lessNodes.next = great.next
        return newHead.next

        