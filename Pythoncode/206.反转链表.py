# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        nodeList = [None]
        while head != None:
            nodeList.append(head)
            head = head.next
        for i in range(len(nodeList)-1, 0, -1):
            nodeList[i].next = nodeList[i-1]
        return nodeList[-1]