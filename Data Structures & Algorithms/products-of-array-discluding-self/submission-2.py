class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]

        temp = 1
        for i in range(len(nums) - 1):
            temp *= nums[i]
            res[i + 1] = temp
        temp = 1
        for i in range(len(nums) - 1, 0, -1):
            print(nums[i])
            temp *= nums[i]
            res[i - 1] *= temp
        return res
        