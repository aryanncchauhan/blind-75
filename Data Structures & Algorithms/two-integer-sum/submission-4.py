class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        # iterate list = O(n)
        for i, num in enumerate(nums):
            com = target - num

            # query hashmap (avg) = O(1)
            if com in hash:
                return [hash[com], i]
            
            hash[num] = i

# tc = O(n) * O(1) = O(n)