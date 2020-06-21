class Solution:
    def isMatch(self, s, p):
        p = self.deldupstar(p)
        dp = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        for j in reversed(range(len(p)+1)):
            for i in reversed(range(len(s)+1)):
                if i == len(s):
                    self.prev = False
                self.prev = self.helper(s, p, dp, i, j) or self.prev
                if j - 1 >= 0 and p[j-1] == "*":
                    dp[i][j-1] = self.prev
        return dp[0][0]

    def deldupstar(self, p):
        i = 0
        j = 0
        p = list(p)
        while j < len(p):
            if p[j] != "*":
                p[i] = p[j]
                i += 1
                j += 1
            else:
                if j+1 >= len(p) or p[j+1] != "*":
                    p[i] = p[j]
                    i += 1
                    j += 1
                else:
                    j += 1
        return "".join(p[:i])

    def helper(self, s, p, dp, s_idx, p_idx):
        if dp[s_idx][p_idx] != None:
            return dp[s_idx][p_idx]
        if len(p) == p_idx and len(s) == s_idx:
            dp[s_idx][p_idx] = True
            return dp[s_idx][p_idx]
        if len(p) == p_idx and len(s) != s_idx:
            dp[s_idx][p_idx] = False
            return dp[s_idx][p_idx]
        if len(p) != p_idx and len(s) == s_idx:
            if p[p_idx] == "*":
                dp[s_idx][p_idx] = dp[s_idx][p_idx+1]
            else:
                dp[s_idx][p_idx] = False
            return dp[s_idx][p_idx]
        
        if p[p_idx] in [s[s_idx], "?"]:
            dp[s_idx][p_idx] = dp[s_idx+1][p_idx+1]
        else:
            dp[s_idx][p_idx] = False
        return dp[s_idx][p_idx]

