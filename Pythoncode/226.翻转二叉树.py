# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root
    def helper(self, root):
        if root == None:
            return None
        left = self.helper(root.left)
        right = self.helper(root.right)
        root.left = right
        root.right = left
        return root