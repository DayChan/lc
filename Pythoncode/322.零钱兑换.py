class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        res = self.helper(coins, amount, dp)
        return -1 if res == float("inf") else res 

    def helper(self, coins, amount, dp):
        if amount == 0:
            return 0
        if amount  < 0:
            return float("inf")
        if amount in dp:
            return dp[amount]
        dp[amount] = min([self.helper(coins, amount - c, dp) for c in coins]) + 1
        return dp[amount]