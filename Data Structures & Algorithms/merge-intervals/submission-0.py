class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            start = result[-1][0]
            end = result[-1][1]
            if(end<intervals[i][0]):
                result.append(intervals[i])
            else:
                result.pop()
                new_start = min(intervals[i][0],start)
                new_end = max(intervals[i][1],end)
                result.append([new_start,new_end])

        return result

        