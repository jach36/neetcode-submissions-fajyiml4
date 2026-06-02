class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums) - 1
        for l in range(len(nums) - 2, -1,-1):
            if nums[l] + l >= g:
                g = l 
        return g == 0