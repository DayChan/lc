class Solution:
    def longestIncreasingPath(self, matrix):
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(self.helper(matrix, i, j, dp, set()), max_path)
        return max_path
    def helper(self, matrix, i, j, dp, visited):
        visited.add((i, j))
        if dp[i][j] != None:
            pass
        else:
            next_max_path = 0
            if (i-1, j) not in visited and i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                next_max_path = max(self.helper(matrix, i-1, j, dp, visited), next_max_path)
            if (i+1, j) not in visited and i+1 < len(matrix) and matrix[i][j] < matrix[i+1][j]:
                next_max_path = max(self.helper(matrix, i+1, j, dp, visited), next_max_path)
            if (i, j-1) not in visited and j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                next_max_path = max(self.helper(matrix, i, j-1, dp, visited), next_max_path)
            if (i, j+1) not in visited and j+1 < len(matrix[0]) and matrix[i][j] < matrix[i][j+1]:
                next_max_path = max(self.helper(matrix, i, j+1, dp, visited), next_max_path)
            dp[i][j] = next_max_path + 1
        visited.remove((i, j))
        return dp[i][j]

s = Solution()
s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])