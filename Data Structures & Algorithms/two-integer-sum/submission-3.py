class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        uni = {}        
        for i in range(len(nums)):
                uni[nums[i]] = i

        for j in range(len(nums)):
            p = target - nums[j]
            if p in uni:
                if(uni[p]!=j):
                    return [j,uni[p]]