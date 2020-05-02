# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(n, 1)

    def helper(self, n, start):
        l = []
        if n == 0:
            l.append(None)
            return l
        if n == 1:
            l.append(TreeNode(start))
            return l
        for i in range(n):
            for left in self.helper(i, start):
                for right in self.helper(n-i-1, i+1+start):
                    root = TreeNode(i+start)
                    root.left = left
                    root.right = right
                    l.append(root)
        return l