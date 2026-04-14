"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start) 

        e  = 0  
        s = 1
        while s < len(intervals):
            if intervals[s].start < intervals[e].end:
                return False
            else:
                s +=1 
                e +=1 
        return True