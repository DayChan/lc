class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        nlen = len(matrix[0])
        mlen = len(matrix)
        i = 0
        j = 0
        res = []
        while mlen > 1 and nlen > 1:
            for _ in range(nlen - 1):
                res.append(matrix[i][j])
                j += 1
            for _ in range(mlen - 1):
                res.append(matrix[i][j])
                i += 1
            for _ in range(nlen - 1):
                res.append(matrix[i][j])
                j -= 1
            for _ in range(mlen - 1):
                res.append(matrix[i][j])
                i -= 1
            mlen -= 2
            nlen -= 2
            i += 1
            j += 1
        if mlen == 0 or nlen == 0:
            pass
        elif mlen == 1 and nlen == 1:
            res.append(matrix[i][j])
        elif nlen > 1:
            for t in range(nlen):
                res.append(matrix[i][j+t])
        elif mlen > 1:
            for t in range(mlen):
                res.append(matrix[i+t][j])
        return res

s  = Solution()
s.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])