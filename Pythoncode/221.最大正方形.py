# class Solution:
#     """
#     https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/
#     """
#     def maximalSquare(self, matrix):
#         dp = {} # d[(i, j)] = 以 maxtrix[i][j] 为右下角的最大的正方形边长
#         maxlen = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 maxlen = max(maxlen, self.getmaximalSquarelen(matrix, i, j, dp))
#         return maxlen * maxlen

#     def getmaximalSquarelen(self, matrix, i, j, dp):
#         if i < 0 or j < 0:
#             return 0
#         if (i, j) in dp:
#             return dp[(i, j)]
#         if matrix[i][j] == "0":
#             dp[(i, j)] = 0
#         else:
#             # innerlen = self.getmaximalSquarelen(matrix, i-1, j-1, dp)
#             # a = 0
#             # while True:
#             #     if a == innerlen + 1:
#             #         break
#             #     if matrix[i][j-a] == "0" or matrix[i-a][j] == "0":
#             #          break
#             #     a += 1
#             # dp[(i, j)] = a -1 + 1
#             dp[(i, j)] = min(self.getmaximalSquarelen(matrix, i-1, j-1, dp), self.getmaximalSquarelen(matrix, i-1, j, dp), self.getmaximalSquarelen(matrix, i, j-1, dp)) + 1
#         return dp[(i, j)]

class Solution:
    """
    上面那种注释掉的解法也对
    参考第85题
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = self.getdp(matrix)
        maxarea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxarea = max(maxarea, self.getmaximalSquareArea(matrix, i, j, dp))
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

    def getmaximalSquareArea(self, matrix, i, j, dp):
        cur_w = dp[(i,j)]
        cur_h = 1
        maxarea = 0
        while cur_w >= cur_h:
            maxarea = cur_h * cur_h
            if i - cur_h < 0:
                break
            else:
                cur_w = min(cur_w, dp[(i - cur_h, j)])
                cur_h += 1
        return maxarea