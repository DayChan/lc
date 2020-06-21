# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxlen = -float("inf")
    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.helper(root)
        return self.maxlen
    def helper(self, root):
        if root == None:
            return 0
        else:
            maxleft = self.helper(root.left)
            maxright = self.helper(root.right)
            self.maxlen = max(self.maxlen, maxright + root.val, maxleft + root.val, maxleft + maxright + root.val, root.val)
            return max(maxright + root.val, maxleft + root.val, root.val)
        