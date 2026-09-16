"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        max_room = 0
        room = 0
        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()
        sptr = 0
        eptr = 0

        while(sptr < len(intervals)):
            if(starts[sptr]<ends[eptr]):
                room += 1
                sptr += 1
                max_room = max(max_room , room)

            else:
                room -=1
                eptr +=1

        return max_room



