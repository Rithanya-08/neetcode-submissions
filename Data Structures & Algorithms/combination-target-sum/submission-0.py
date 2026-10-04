class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] 
        def solve(i,temp,target):
            
            if(target == 0):
                result.append(temp[:])
                return 
            if(i>=len(nums) or target<0):
                return 

            temp.append(nums[i])
            solve(i,temp,target-nums[i])
            temp.pop()
            solve(i+1,temp,target)
        solve(0,[],target)
        return result
            