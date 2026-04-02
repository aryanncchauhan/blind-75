class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) < 3:
            return []

        nums.sort()

        def twoSum(target, i):
            lo = i + 1
            hi = len(nums) - 1

            while True:
                if lo >= hi:
                    return
                if nums[lo] + nums[hi] < target:
                    lo += 1
                elif nums[lo] + nums[hi] > target:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            twoSum(0 - num, i)

        return res

        