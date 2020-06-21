# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int):
       solu = []
       self.helper(root, [], target, solu)
       return solu

    def helper(self, root, seq, target, solu):
        if root == None:
            return
        seq.append(root.val)
        if root.left == None and root.right == None:
            if sum(seq) == target:
                solu.append(seq)
        else:
            self.helper(root.left, seq.copy(), target, solu)
            self.helper(root.right, seq.copy(), target, solu)

root = TreeNode(-2)
root.right = TreeNode(-3)
s = Solution()
j = s.pathSum(root, -2)