class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # iterate list = O(n)
        for num in nums:
            # set operations (average) = O(1)
            if num in seen:
                return True
            seen.add(num)

        return False

# tc = O(n) * O(1) = O(n)