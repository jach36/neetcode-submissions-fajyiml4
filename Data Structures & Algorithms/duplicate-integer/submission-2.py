class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if i in store.keys():
                return True
            else:
                store[i] = 1
        return False
