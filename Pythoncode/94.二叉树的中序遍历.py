# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        self.helper(root, l)
        return l

    def helper(self, node, l):
        if node != None:
            if node.left != None:
                self.helper(node.left, l)
            l.append(node.val)
            if node.right != None:
                self.helper(node.right, l)
            