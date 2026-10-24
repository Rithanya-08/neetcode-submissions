class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def solve(i,temp):
            if(i>= len(nums)):
                result.append(temp[:])
                return
            if(i< len(nums)):
                result.append(temp[:])
            
            for j in range(i,len(nums)):
                if(j == i or nums[j] != nums[j-1]):
                    temp.append(nums[j])
                    solve(j+1,temp)
                    temp.pop()

        solve(0,[])
        return result