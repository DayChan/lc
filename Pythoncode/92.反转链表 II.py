# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        res = head
        reverseStack = []
        i = 1
        while i < m:
            head = head.next
            i += 1
        while i <= (m + n) // 2:
            reverseStack.append(head)
            head = head.next
            i += 1
        if i > (m + n + 1) // 2:
            reverseStack.pop()
        while len(reverseStack) != 0:
            head.val, reverseStack[-1].val = reverseStack[-1].val, head.val
            reverseStack.pop()
            head = head.next
        return res