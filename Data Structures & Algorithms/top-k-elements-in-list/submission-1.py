import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use min heaps to store only k elements - sorting is not necessary here
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] =1

        heap = []
        for num,count in dic.items():
            heapq.heappush(heap,(count,num))

            if(len(heap)>k):
                heapq.heappop(heap)

        return [num for count,num in heap]
