class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort(key = lambda x: x[0])
        curr = intervals[0]
        print(intervals)
        for i in range(1,len(intervals)):
            if curr[1] >= intervals[i][0]:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
            else:
                res.append(curr)
                curr = intervals[i]
        res.append(curr)
        return res