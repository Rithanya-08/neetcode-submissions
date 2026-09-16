class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[1],x[0]))
        print(intervals)
        result = [intervals[0]]
        count = 0
        for i in range(1,len(intervals)):
            start,end = result[-1]
            if(intervals[i][0]>=end):
                result.append(intervals[i])
            else:
                count+=1
        return count

