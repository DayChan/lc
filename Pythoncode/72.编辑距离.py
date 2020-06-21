class Solution:
    """
    https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
    dp[i][j] 代表 word1[:i] 位置转换成 word2[:j] 位置需要最少步数
    所以，
    当 word1[:i][-1] == word2[:j][-1]，dp[i][j] = dp[i-1][j-1]；
    当 word1[:i][-1] != word2[:j][-1]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。

    对“dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。”的补充理解：
    以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为 word2的前 3 个字符，也就是将 horse 转换为 ros，因此有：
    (1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）
    (2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作
    (3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符

    """
    def minDistance(self, word1: str, word2: str) -> int:
        d = {}
        for j in range(len(word2)+1):
            d[(0, j)] = j
        for i in range(len(word1)+1):
            d[(i, 0)] = i
        return self.getminDistance(word1, word2, len(word1), len(word2), d)
    
    def getminDistance(self, word1, word2, i, j, d):
        if (i, j) in d:
            pass
        else:
            if word1[:i][-1] == word2[:j][-1]:
                d[(i, j)] = self.getminDistance(word1, word2, i-1, j-1, d)
            else:
                d[(i, j)] = min(self.getminDistance(word1, word2, i-1, j, d), self.getminDistance(word1, word2, i-1, j-1, d), self.getminDistance(word1, word2, i, j-1, d)) + 1
        
        return d[(i, j)]