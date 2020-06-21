# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -999999999999, 999999999999)
        
    def helper(self, root, base, bound):
        if root == None:
            return True
        if root.val <= base or root.val >= bound:
            return False
        return self.helper(root.left, base, root.val) and self.helper(root.right, root.val, bound)