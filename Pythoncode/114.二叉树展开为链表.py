# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None, None
        lefthead, lefttail = self.flatten(root.left)
        righthead, righttail = self.flatten(root.right)
        root.left = None
        root.right = None
        reshead, restail = root, root
        if lefthead != None:
            restail.right = lefthead
            restail = lefttail
        if righthead != None:
            restail.right = righthead
            restail = righttail
        return reshead, restail
        
s = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(5)
r.left.left = TreeNode(3)
r.left.right = TreeNode(4)
r.right.right = TreeNode(6)
s.flatten(r)