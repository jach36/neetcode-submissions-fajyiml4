class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        res = []
        temp = [None for i in range(len(nums))]
        
        for n in set(nums):
            ind = len(temp) - nums.count(n)
            if temp[ind] is None:
                temp[ind] = [n]
            else:   
                temp[ind].append(n)
        
            
        for t in temp: 
            if len(res) == k:
                return res
            if t is not None:
                for i in t:
                    res.append(i)
        return res