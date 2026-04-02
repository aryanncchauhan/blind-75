class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        mySet = set(nums)

        for num in nums:
            if num - 1 not in mySet:
                currLen = 1
                target = num + 1
                while True:
                    if target in mySet:
                        currLen += 1
                        target += 1
                    else:
                        break
                
                maxLen = max(maxLen, currLen)

        return maxLen

        