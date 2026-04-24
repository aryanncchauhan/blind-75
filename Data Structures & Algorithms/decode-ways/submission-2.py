class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        if 0 < int(s[0]) < 10:
            dp[0] = 1

        for i in range(1, n):
            if 0 < int(s[i]) < 10:
                dp[i] += dp[i - 1]

            if 9 < int(s[i - 1 : i + 1]) < 27:
                dp[i] += (dp[i - 2] if i >= 2 else 1)

        return dp[-1]