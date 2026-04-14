"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals
        # intervals.sort(key=lambda x = x.start)

        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        
        maxrm = 0 
        rooms = 0 

        s, e = 0, 0 
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else: 
                rooms -= 1
                e += 1
            maxrm = max(maxrm, rooms)
        return maxrm