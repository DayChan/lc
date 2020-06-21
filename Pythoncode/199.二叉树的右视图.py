# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = []
        q = [root]
        while len(q) != 0:
            newq = []
            for node in q:
                if node.left != None:
                    newq.append(node.left)
                if node.right != None:
                    newq.append(node.right)
            res.append(q[-1].val)
            q = newq
        return res