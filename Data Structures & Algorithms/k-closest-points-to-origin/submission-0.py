import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []
        for x,y in points:
            dist = (x**2 + y**2)
            heapq.heappush(min_heap,(dist,[x,y]))

        for i in min_heap[:k]:
            curr = heapq.heappop(min_heap)
            result.append(curr[1])

        return result

