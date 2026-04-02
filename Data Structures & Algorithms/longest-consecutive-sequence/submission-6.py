import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        map = {}
        minVal = min(nums)
        print("min = " + str(minVal))
        maxVal = max(nums)
        print("max = " + str(maxVal))

        for num in nums:
            map[num] = True

        currLen = 1
        maxLen = 1
        
        for i in range(minVal + 1, maxVal + 1):
            if i in map:
                currLen += 1
            else:
                currLen = 0
            maxLen = max(currLen, maxLen)

        return maxLen