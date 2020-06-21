# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.buildTree(nums)
    
    def buildTree(self, nums):
        if len(nums) == 0:
            return None
        else:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.buildTree(nums[:mid])
            root.right = self.buildTree(nums[mid+1:])
            return root