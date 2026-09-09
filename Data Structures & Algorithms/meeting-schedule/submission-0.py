"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start) #advanced ting

        for j in range(1, len(intervals)):
            i1 = intervals[j-1]
            i2 = intervals[j]

            if i1.end > i2.start:
                return False
        
        return True


