class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDictSet = set()
        for word in wordDict:
            wordDictSet.add(word)
        dp = {}
        return self.checkBreakable(s, wordDictSet, dp)
    def checkBreakable(self, s, wordDictSet, dp):
        if s in dp:
            return dp[s]
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if self.checkBreakable(s[:i], wordDictSet, dp) and s[i:] in wordDictSet:
                dp[s] = True
                return dp[s]
        dp[s] = False
        return dp[s]
