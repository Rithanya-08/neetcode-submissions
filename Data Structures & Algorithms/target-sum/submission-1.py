class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def solve(i,rem):
            if(i==n):
                if(rem == 0):
                    return 1
                else:
                    return 0
                    
            if((i,rem) in dp):
                return dp[(i,rem)]

            take = solve(i+1,rem - nums[i])
            skip = solve(i+1,rem + nums[i])   

            dp[(i,rem)] = take + skip

            return dp[(i,rem)]

        return solve(0,target)