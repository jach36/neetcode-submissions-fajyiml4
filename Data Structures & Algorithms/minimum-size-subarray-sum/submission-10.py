class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 1 
        summ = 0
        min_len = float("inf")

        for r in range(len(nums)):
            summ += nums[r]   
            while summ >= target:
                min_len = min(min_len, r - l + 1)
                summ -= nums[l]
                l += 1

        return 0 if min_len == float("inf") else min_len
