class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        l, r = 0, 0
        mySet = set()
        
        while r < len(s):
            if s[r] in mySet:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    l += 1
            
            mySet.add(s[r])
            size = r - l + 1
            maxLen = max(maxLen, size)

            r += 1
        
        return maxLen