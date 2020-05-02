# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if TreeNode == None:
            return True
        line = []
        line.append(root)
        while len(line) != 0:
            if self.checkline(line) == False:
                return False
            newline = []
            for node in line:
                if node == None:
                    pass
                else:
                    newline.append(node.left)
                    newline.append(node.right)
            line = newline
        return True

    def checkline(self, line):
        i = 0
        j = len(line) - 1
        while j > i:
            if (line[j] == None and line[i] == None) or (line[j] != None and line[i] != None and line[j].val == line[i].val):
                i += 1
                j += 1
            else:
                return False
        return True