class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0 
        maximum = nums[0]

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                maximum = max(maximum, i + nums[i])
            l = r + 1
            r = maximum 
            res += 1
        return res 