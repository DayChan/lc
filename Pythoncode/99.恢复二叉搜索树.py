# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        用中序遍历树，并将所有节点存到一个一维向量中，
        把所有节点值存到另一个一维向量中，(如果是正常的BST，将已经从小到大排好顺序了)
        然后对存节点值的一维向量排序，在将排好的数组按顺序赋给节点。
        """
        self.nodes = []
        self.vals = []
        self.inorder(root)
        insertionSort(self.vals)
        for i, val in enumerate(self.vals):
            self.nodes[i].val = val

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.nodes.append(node)
        self.vals.append(node.val)
        self.inorder(node.right)


r = TreeNode(1)
r.left = TreeNode(3)
r.left.right = TreeNode(2)

s = Solution()
s.recoverTree(r)
