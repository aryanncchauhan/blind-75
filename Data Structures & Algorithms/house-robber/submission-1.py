class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [[0] * 2 for _ in range(len(nums))]

        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        for i in range(len(nums)):
            print(f"{i}")
            print(f"dp[{i}][0] = {dp[i][0]}")
            print(f"dp[{i}][1] = {dp[i][1]}")
            print("")

        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])