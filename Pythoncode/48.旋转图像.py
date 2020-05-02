class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        j = 0
        while n > 1:
            for t in range(n - 1):
                tmp1 = matrix[i][j+t]
                tmp2 = matrix[i+t][j+n-1]
                tmp3 = matrix[i+n-1][j+n-1-t]
                tmp4 = matrix[i+n-1-t][j]
                matrix[i+t][j+n-1] = tmp1
                matrix[i+n-1][j+n-1-t] = tmp2
                matrix[i+n-1-t][j] = tmp3
                matrix[i][j+t] = tmp4
            n -= 2
            i += 1
            j += 1
