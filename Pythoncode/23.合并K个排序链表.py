from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        compnodeq= PriorityQueue()
        for index, node in enumerate(lists):
            if node != None:
                compnodeq.put((node.val, index, node)) # https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
        orderednodes = []
        while not compnodeq.empty():
            val, index, minnode = compnodeq.get()
            orderednodes.append(minnode)
            if minnode.next != None:
                compnodeq.put((minnode.next.val, index, minnode.next))
        for i in range(len(orderednodes) - 1):
            orderednodes[i].next = orderednodes[i+1]
        if len(orderednodes) == 0:
            return None
        orderednodes[-1].next = None
        return orderednodes[0]
