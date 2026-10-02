class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(i,temp):
            if(i>=len(nums)):
                result.append(temp[:])
                return
            
            temp.append(nums[i])
            solve(i+1,temp)
            temp.pop()
            solve(i+1,temp)

        solve(0,[])
        return result

        