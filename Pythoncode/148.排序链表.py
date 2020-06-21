# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    模拟了快速排序
    """
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        headnode, _ = self.helper(head)
        return headnode
    def helper(self, head):
        if head.next == None:
            return head, head
        else:
            curnode = head
            head = head.next
            curnode.next = None
            lefthead = None
            righthead = None
            leftlen = 0
            rightlen = 0
            while head != None:
                node = head
                head = head.next
                if node.val < curnode.val:
                    node.next = lefthead
                    lefthead = node
                    leftlen += 1
                elif node.val > curnode.val:
                    node.next = righthead
                    righthead = node
                    rightlen += 1
                elif leftlen <= rightlen: #使相同大小的数左右数量均匀
                    node.next = lefthead
                    lefthead = node
                    leftlen += 1
                else:
                    node.next = righthead
                    righthead = node
                    rightlen += 1
            if lefthead != None:
                lefthead, lefttail = self.helper(lefthead)
                finalhead = lefthead
                lefttail.next = curnode
            else:
                finalhead = curnode
            if righthead != None:
                righthead, righttail = self.helper(righthead)
                finaltail = righttail
                curnode.next = righthead
            else:
                finaltail = curnode
            return finalhead, finaltail