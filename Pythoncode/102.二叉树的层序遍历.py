# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        level2list = {}
        levels = [0]
        nodes = [root]
        l = []
        while len(nodes) != 0:
            node = nodes[0]
            nodes = nodes[1:]
            level = levels[0]
            levels = levels[1:]
            if node.left != None:
                nodes.append(node.left)
                levels.append(level+1)
            if node.right != None:
                nodes.append(node.right)
                levels.append(level+1)
            if level not in level2list.keys():
                level2list[level] = []
            level2list[level].append(node.val)
        for level in sorted(level2list.keys()):
            l.append(level2list[level])
        return l