class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            self.twoSum(nums[i + 1 :], target, res)
        return [list (triplet) for triplet in res]

        
    def twoSum(self, nums: List[int], target: int, res: set) -> None:
        numSet = set()
        for num in nums:
            complement = target - num
            if complement in numSet:
                sol = [-1 * target, num, complement]
                sol = sorted(sol)
                tupleSol = tuple(sol)
                res.add(tupleSol)
            else:
                numSet.add(num)