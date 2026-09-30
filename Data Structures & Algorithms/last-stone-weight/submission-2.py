import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lis = []
        for i in stones:
            heapq.heappush(lis,-i)
        
        while(len(lis) >1):
            heapq.heapify(lis)
            first = heapq.heappop(lis)
            second = heapq.heappop(lis)

            if(first > second):
                heapq.heappush(lis,-first+second)
            elif(second > first):
                heapq.heappush(lis,-second+first)

        if(lis):
            return -heapq.heappop(lis)
        else:
            return 0
