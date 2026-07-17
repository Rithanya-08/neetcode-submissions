class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] =1

        # We can use the bucket sort algorithm
        arr = [[] for _ in range(len(nums)+1)]
        
        for nums,count in dic.items():
            arr[count].append(nums)

        res = []

        for p in arr[::-1]:
            if(len(p)<=k):
                res.extend(p)

            k-=len(p)

        return res

