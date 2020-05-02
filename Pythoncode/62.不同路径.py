class Solution:
    def countPaths(self, index2NumofPaths, m, n, x, y):
        if (x, y) in index2NumofPaths.keys():
            return index2NumofPaths[(x, y)]
        if x == 0 and y == 0:
            index2NumofPaths[(x, y)] = 1
            return 1
        elif x < 0 or x >= m or y < 0 or y >= n:
            index2NumofPaths[(x, y)] = 0
            return 0
        else:
            index2NumofPaths[(x, y)] = self.countPaths(index2NumofPaths, m, n, x-1, y) + self.countPaths(index2NumofPaths, m, n, x, y-1)
            return index2NumofPaths[(x, y)]

    def uniquePaths(self, m: int, n: int) -> int:
        index2NumofPaths = {}
        return self.countPaths(index2NumofPaths, m, n, m-1, n-1)

s = Solution()
print(s.uniquePaths(23, 12))