class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def helper(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]

            dp = [[0] * 2 for _ in range(len(nums))]

            dp[0][0] = 0
            dp[0][1] = houses[0]

            for i in range(1, len(houses)):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = dp[i - 1][0] + houses[i]

            return max(dp[len(houses) - 1][0], dp[len(houses) - 1][1])

        return max(helper(nums[0:len(nums) - 1]), helper(nums[1:len(nums)]))