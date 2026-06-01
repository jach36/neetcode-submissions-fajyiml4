class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return nums[0]

        count = 0
        maxCount = nums[0]

        for n in nums:
            if count <= 0:
                count = 0
            count += n 
            maxCount = max(maxCount, count)

        return maxCount


