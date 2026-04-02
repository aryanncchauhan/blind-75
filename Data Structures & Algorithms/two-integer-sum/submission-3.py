class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            com = target - num

            if com in hash:
                return [hash[com], i]
            
            hash[num] = i