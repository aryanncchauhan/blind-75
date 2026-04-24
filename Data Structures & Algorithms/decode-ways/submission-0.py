class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        def oneDigitCheck(x):
            return 0 < x < 10

        def twoDigitCheck(x):
            return 9 < x < 27

        if oneDigitCheck(int(s[0])):
            dp[0] = 1

        for i in range(1, n):
            oneDigit = int(s[i])
            twoDigit = int(s[i - 1: i + 1])

            if oneDigitCheck(oneDigit):
                dp[i] += dp[i - 1]

            if twoDigitCheck(twoDigit):
                dp[i] += (dp[i - 2] if i >= 2 else 1)

        return dp[-1]