class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = {} # d[(i, j)] = text1[:i] 和 text2[:j]之间的最长公共子序列
        maxcomsublen = 0
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                maxcomsublen = max(maxcomsublen, self.getMaxComSublen(text1, text2, i, j, d))
        return maxcomsublen

    def getMaxComSublen(self, text1, text2, i, j, d):
        if i == 0 or j == 0:
            return 0
        if (i, j) in d:
            return d[(i, j)]
        if text1[:i][-1] != text2[:j][-1]:
            d[(i, j)] = max(self.getMaxComSublen(text1, text2, i-1, j, d), self.getMaxComSublen(text1, text2, i, j-1, d))
        else:
            d[(i, j)] = 1 + self.getMaxComSublen(text1, text2, i-1, j-1, d)
        return d[(i, j)]

