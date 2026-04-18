class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0 
        
        intervals.sort(key = lambda x : x[0])
        curr = intervals[0]

        for i in range(1, len(intervals)):
            nxt = intervals[i]
            # means overlapping
            if curr[1] > nxt[0]:
                # if nxt[0] < curr[0]:
                if curr[1] > nxt[1]:
                    curr = nxt
                count += 1
            else:
                curr = nxt
                
        return count