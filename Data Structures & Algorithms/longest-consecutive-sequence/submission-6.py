class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_sorted = sorted(set(nums))
        if len(nums_sorted) == 0 or len(nums_sorted) == 1:
            return len(nums_sorted)

        record = 0
        temp = 1


        for i in range(len(nums_sorted) - 1):
            if (nums_sorted[i] + 1) == nums_sorted[i + 1]:
                temp += 1
            else:
                temp = 1
            record = max(record, temp)
        return record 