class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0

        mySet = set(nums)

        for i, num in enumerate(nums):
            currLen = 1
            for j in range(num + 1, num + 1 + len(nums)):
                if j in mySet:
                    currLen += 1
                else:
                    break
            maxLen = max(maxLen, currLen)
            
        return maxLen