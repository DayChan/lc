class Solution:
    def numIslands(self, grid):
        islandnum = 0
        landset = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                else:
                    if (i, j) not in landset:
                        islandnum += 1
                        self.createIsland(i, j, landset, grid)
        return islandnum
    def createIsland(self, i, j, landset, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or (i, j) in landset:
            return
        else:
            landset.add((i, j))
            self.createIsland(i-1, j, landset, grid)
            self.createIsland(i+1, j, landset, grid)
            self.createIsland(i, j-1, landset, grid)
            self.createIsland(i, j+1, landset, grid)
s = Solution()
s.numIslands([["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]])