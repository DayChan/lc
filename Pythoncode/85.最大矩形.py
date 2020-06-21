class Solution:
    """
    https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/
    """
    def maximalRectangle(self, matrix):
        dp = self.getdp(matrix)
        maxarea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxarea = max(maxarea, self.getmaximalRectangleArea(matrix, i, j, dp))
        return maxarea
    
    def getdp(self, matrix):
        dp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    count = 0 #init
                if matrix[i][j] == "0":
                    count = 0 #reset
                else:
                    count += 1 #increase
                dp[(i, j)] = count
        return dp
    
    def getmaximalRectangleArea(self, matrix, i, j, dp):
        cur_w = dp[(i,j)]
        cur_h = 1
        maxarea = cur_w * cur_h
        while i - cur_h >= 0 and dp[(i - cur_h, j)] != 0:
            cur_w = min(cur_w, dp[(i - cur_h, j)])
            cur_h += 1
            maxarea = max(maxarea, cur_h * cur_w)
        return maxarea

