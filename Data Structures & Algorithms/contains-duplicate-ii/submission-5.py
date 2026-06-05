class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, len(nums) - 1

        while r > l:
            right = nums[r]
            left = nums[l]
            if right == left and r - l <= k :
                return True 
            if r - l > k:
                l += 1 
            else: 
                r -= 1
        return False