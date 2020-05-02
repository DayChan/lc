class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        return self.helper(n, d)
    def helper(self, n, d):
        if n in d:
            return d[n]
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            d[n] = self.helper(n-1, d) + self.helper(n-2, d)
            return d[n]
