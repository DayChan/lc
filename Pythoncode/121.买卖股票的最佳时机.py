class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [0] # dp[i] = 若第i天卖出，能获得的最大收益（若同一天买入，同一天卖出，则收益为0）
        minprice = prices[0] # 前i天（包括第i天）之中，最低的股票价格
        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i])
            dp.append(prices[i] - minprice)
        return max(dp)