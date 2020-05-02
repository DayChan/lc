class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        maxlen = 0
        maxpair = None
        ifPalindrome = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 > maxlen and self.isPalindrome(ifPalindrome, s, i, j):
                    maxlen = j - i + 1
                    maxpair = (i, j)
        return s[maxpair[0]:maxpair[1]+1]
    
    def isPalindrome(self, ifPalindrome, s, i, j):
        if i == j or j < i:
            return True
        elif (i, j) in ifPalindrome:
            return ifPalindrome[(i, j)]
        else:
            ifPalindrome[(i, j)] =  s[i] == s[j] and self.isPalindrome(ifPalindrome, s, i+1, j-1)
            return ifPalindrome[(i, j)]


s = Solution()
s.longestPalindrome("babad")