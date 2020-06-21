class Solution:
    def __init__(self):
        self.n2numTrees = {}
        self.n2numTrees[0] = 1

    def numTrees(self, n: int) -> int:
        if n in self.n2numTrees.keys():
           return self.n2numTrees[n]
        s = 0
        for i in range(n):
            s += self.numTrees(i) * self.numTrees(n-i-1)
        self.n2numTrees[n] = s
        return s
