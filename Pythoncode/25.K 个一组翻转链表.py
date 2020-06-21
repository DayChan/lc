# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        headnode = head
        tailnode = head
        prevnode = None
        count = 1
        while tailnode != None:
            if count == k:
                nextnode = tailnode.next
                newheadnode, newtailnode = self.reverse(headnode, tailnode)
                if prevnode != None:
                    prevnode.next = newheadnode
                else:
                    head = newheadnode
                newtailnode.next = nextnode
                headnode = newtailnode.next
                tailnode = newtailnode.next
                prevnode = newtailnode
                count = 1
            else:
                tailnode = tailnode.next
                count += 1
        return head
    
    def reverse(self, headnode, tailnode):
        newtailnode = headnode
        newheadnode = headnode
        while newheadnode != tailnode:
            passedheadnode = newheadnode
            newheadnode = newtailnode.next
            newtailnode.next = newheadnode.next
            newheadnode.next = passedheadnode
        return newheadnode, newtailnode
