class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, len(nums) - 1

        while r > l:
            right = nums[r]
            left = nums[l]
            if r - l <= k:
                if right == left:
                    return True 
                r -= 1
            else: 
                l += 1
        return False