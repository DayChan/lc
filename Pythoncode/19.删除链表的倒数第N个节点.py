# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        delnode = head
        prevdelnode = None
        lastnode = head
        while n > 1:
            lastnode = lastnode.next
            n -= 1
        while lastnode.next != None:
            lastnode = lastnode.next
            prevdelnode = delnode
            delnode = delnode.next
        if prevdelnode != None:
            prevdelnode.next = delnode.next
        else:
            head = head.next
        return head