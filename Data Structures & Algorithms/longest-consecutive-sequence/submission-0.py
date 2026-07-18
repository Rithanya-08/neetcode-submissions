class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        maxl = 0
        for i in range(len(nums)):
            dic[nums[i]] = i

        for j in nums:
            if(j-1 in nums):
                continue
            else:
                count = 1
                current = j+1

                while current in dic:
                    current+=1
                    count+=1

                maxl = max(maxl,count)

        return maxl
