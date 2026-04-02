class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        productsFromLeft = [0] * len(nums)
        productsFromRight = [0] * len(nums)

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            productsFromLeft[i] = product

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            productsFromRight[i] = product

        for i in range(-1, len(nums) - 1):
            j = i + 2

            product = 1

            if i in range(len(nums)):
                product *= productsFromLeft[i]
            
            if j in range(len(nums)):
                product *= productsFromRight[j]

            res.append(product)

        return res