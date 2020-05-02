class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # dp[(a, b, c)] = 代表当第a天结束时；从第0天开始到第a天结束，至多进行了b次买入；且当前状态时c(1持有股票， 0不持有股票)；的最大总资产(指有多少钱)
        return self.getmaxProfit(prices, len(prices)-1, len(prices)//3 + 1, 0, dp)
    def getmaxProfit(self, prices, a, b, c, dp):
        if b == 0 or a < 0:
            return 0
        if a == 0:
            if c == 1:
                return - prices[a]
            else:
                return 0
        
        # 一个优化 不然会超时
        b = min(b, a // 3 + 1)
        
        if (a, b, c) in dp:
           pass
        elif c == 1: #第a天结束时持有股票
            p1 = self.getmaxProfit(prices, a-1, b, 1, dp) #第a-1天结束时就已经持有股票，第a天什么也没干
            p2 = self.getmaxProfit(prices, a-2, b-1, 0, dp) - prices[a] #第a-1天结束时就还没有持有股票，且必须第a-1天什么也没干，所以第a-2天结束时不持有股票， 第a天才买入股票，所以从第0天开始到第a-1天结束，只能至多进行了b-1次买入
            dp[(a, b, c)] = max(p1, p2)
        else: #第a天结束时不持有股票
            p1 = self.getmaxProfit(prices, a-1, b, 0, dp) #第a-1天结束时也不持有股票，第a天什么也没干
            p2 = self.getmaxProfit(prices, a-1, b, 1, dp) + prices[a] #第a-1天结束时持有股票，第a天把股票卖出
            dp[(a, b, c)] = max(p1, p2)
        
        return dp[(a, b, c)]
        