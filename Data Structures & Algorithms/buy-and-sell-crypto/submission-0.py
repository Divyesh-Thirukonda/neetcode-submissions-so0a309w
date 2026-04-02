class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minP = prices[0]
        maxProfit = 0

        for i, price in enumerate(prices):
            minP = min(minP, price)
            maxProfit = max(maxProfit, price - minP)

        return maxProfit