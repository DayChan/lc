# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        while l1 != None:
            s1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            s2 += str(l2.val)
            l2 = l2.next
        n1 = int(s1)
        n2 = int(s2)
        n = n1 + n2
        s = str(n)
        head = ListNode(int(s[0]))
        p = head
        s = s[1:]
        for i in range(len(s)):
            p.next = ListNode(int(s[i]))
            p = p.next
        return head