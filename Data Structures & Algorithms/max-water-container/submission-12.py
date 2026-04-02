class Solution:
    def maxArea(self, heights: List[int]) -> int:
        print(len(heights))
        maxArea = 0
        
        l = 0
        r = len(heights) - 1
        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(currArea, maxArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea
