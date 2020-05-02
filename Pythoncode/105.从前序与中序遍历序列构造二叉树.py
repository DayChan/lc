# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        https://www.tianmaying.com/tutorial/LC105
        """
        if len(preorder) == 0:
            return None
        rootNode = TreeNode(preorder[0])
        index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree(preorder[1:index+1], inorder[:index])
        rootNode.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return rootNode