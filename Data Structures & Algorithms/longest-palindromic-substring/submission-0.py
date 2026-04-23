class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start, maxLen = 0, 1

        # len == 1
        for i in range(n):
            dp[i][i] = True

        # len == 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, maxLen = i, 2

        # len >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > maxLen:
                        start, maxLen = i, length

        return s[start : start + maxLen]