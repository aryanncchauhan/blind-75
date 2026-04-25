class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1

        for i in range(1, amount + 1):
            minAmt = float("inf")
            for coin in coins:
                if (i - coin) >= 0 and dp[i - coin] != -1:
                    minAmt = min(minAmt, dp[i - coin])

            if minAmt == float("inf"):
                dp[i] = -1
            else:
                dp[i] = minAmt + 1

        return dp[-1]