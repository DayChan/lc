# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxlength = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.maxlength
    def helper(self, root):
        if root == None:
            return -1
        leftmaxlength = self.helper(root.left)
        rightmaxlength = self.helper(root.right)
        self.maxlength = max(self.maxlength, leftmaxlength+1+rightmaxlength+1)
        return max(leftmaxlength+1, rightmaxlength+1)
        