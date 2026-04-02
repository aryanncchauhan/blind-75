import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numsSet = set(nums)

        maxLen = 0

        for i in range(len(nums)):
            currLen = 0
            if nums[i] - 1 not in numsSet:
                j = nums[i]
                while j in numsSet:
                    currLen += 1
                    j += 1
                maxLen = max(currLen, maxLen)

        return maxLen
