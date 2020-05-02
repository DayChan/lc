class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hasstock = False
        hasmoney = 0
        for i in range(len(prices)-1):
            if hasstock == False and prices[i+1] > prices[i]:
                hasstock = True
                hasmoney -= prices[i]
            elif hasstock == False and prices[i+1] <= prices[i]:
                pass
            elif hasstock == True and prices[i+1] <= prices[i]:
                hasstock = False
                hasmoney += prices[i]
            else:
                pass
        if hasstock:
            hasstock = False
            hasmoney += prices[-1]
        return hasmoney
