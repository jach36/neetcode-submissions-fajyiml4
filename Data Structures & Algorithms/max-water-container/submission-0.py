class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxHeight = 0

        while l < r:
            height = min(heights[r], heights[l])
            width = r - l

            maxHeight = max(maxHeight, height * width)  

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxHeight 