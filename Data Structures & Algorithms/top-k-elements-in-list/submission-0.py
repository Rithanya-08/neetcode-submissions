class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] =1

        # Brute force approach
        lst = list(dic.items())
        lst.sort(key = lambda x:x[1],reverse = True)
        res = []
        for p in range(k):
            res.append(lst[p][0])

        return res

