class Solution:
    def minPathSum(self, grid):
        d = {}
        return self.helper(grid, len(grid)-1, len(grid[0])-1, d)
    def helper(self, grid, i, j, d):
        if (i, j) in d:
            return d[(i, j)]
        if i < 0 or j < 0:
            return None
        left = self.helper(grid, i-1, j, d)
        up = self.helper(grid, i, j-1, d)
        if left == None and up == None:
            d[(i, j)] = grid[i][j]
        elif left == None and up != None:
            d[(i, j)] = grid[i][j] + up
        elif up == None and left != None:
             d[(i, j)] = grid[i][j] + left
        else:
             d[(i, j)] = grid[i][j] + min(left, up)
        return d[(i, j)]
s = Solution()
s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])