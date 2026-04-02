class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force sol: 
        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         max_profit = max(max_profit, prices[j] - prices[i])

        # return max_profit

        # two pointers:
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            
            r += 1
        
        return max_profit

