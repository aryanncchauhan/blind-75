class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                currProfit = prices[j] - prices[i]
                maxProfit = max(currProfit, maxProfit)
        return maxProfit
        