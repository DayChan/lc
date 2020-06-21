# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeLists = []
        while l1 != None or l2 != None:
            if l1 == None:
                nodeLists.append(l2)
                l2 = l2.next
            elif l2 == None:
                nodeLists.append(l1)
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    nodeLists.append(l1)
                    l1 = l1.next
                else:
                    nodeLists.append(l2)
                    l2 = l2.next
        for i in range(len(nodeLists)-1):
            nodeLists[i].next = nodeLists[i+1]
        return nodeLists[0] if nodeLists else None
