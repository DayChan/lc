# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        head = TreeNode(postorder[-1])
        index = inorder.index(head.val)
        head.left = self.buildTree(inorder[:index], postorder[:index])
        head.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return head

s = Solution()
print(s.buildTree([9,3,15,20,7], [9,15,7,20,3]).val)