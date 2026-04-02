class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting = O(nlog(n))
        return sorted(s) == sorted(t)
        
# tc = O(nlog(n))